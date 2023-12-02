import json
import os

from PySide6.QtWidgets import QPushButton,QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QPen, QColor, QMouseEvent
from PySide6.QtCore import Qt, QRectF, QPointF, QEvent, QSizeF


class ResizableRectItem(QGraphicsRectItem):
    handleSize = +8.0
    handleSpace = -4.0
    handleCursors = {
        1: Qt.SizeFDiagCursor,
        2: Qt.SizeVerCursor,
        3: Qt.SizeBDiagCursor,
        4: Qt.SizeHorCursor,
        6: Qt.SizeHorCursor,
        7: Qt.SizeBDiagCursor,
        8: Qt.SizeVerCursor,
        9: Qt.SizeFDiagCursor,
    }

    def __init__(self, *args):
        super(ResizableRectItem, self).__init__(*args)
        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setFlag(QGraphicsRectItem.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.ItemIsSelectable)
        self.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.updateHandlesPos()

    def setGeometry(self, rect):
        self.setRect(rect)
        self.updateHandlesPos()

    def handleAt(self, point):
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        if self.isSelected() and not moveEvent.modifiers() & Qt.ControlModifier:
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super(ResizableRectItem, self).hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        self.setCursor(Qt.ArrowCursor)
        super(ResizableRectItem, self).hoverLeaveEvent(moveEvent)

    def mousePressEvent(self, mouseEvent):
        self.handleSelected = self.handleAt(mouseEvent.pos())
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super(ResizableRectItem, self).mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            super(ResizableRectItem, self).mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        super(ResizableRectItem, self).mouseReleaseEvent(mouseEvent)
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()

    def boundingRect(self):
        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        s = self.handleSize
        b = self.boundingRect()
        self.handles[1] = QRectF(b.left(), b.top(), s, s)
        self.handles[2] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[3] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[4] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[6] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[7] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[8] = QRectF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[9] = QRectF(b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        rect = self.rect()
        diff = mousePos - self.mousePressPos
        self.prepareGeometryChange()

        if self.handleSelected == 1:
            rect.setTopLeft(rect.topLeft() + diff)
        elif self.handleSelected == 3:
            rect.setTopRight(rect.topRight() + diff)
        elif self.handleSelected == 7:
            rect.setBottomLeft(rect.bottomLeft() + diff)
        elif self.handleSelected == 9:
            rect.setBottomRight(rect.bottomRight() + diff)

        self.setRect(rect)
        self.updateHandlesPos()
        self.mousePressPos = mousePos

    def paint(self, painter, option, widget=None):
        super(ResizableRectItem, self).paint(painter, option, widget)
        painter.setPen(QPen(QColor(0, 100, 255), 1))
        painter.setBrush(QColor(0, 100, 255, 100))

        if self.isSelected():
            painter.setPen(QPen(QColor(0, 100, 255), 0))
            painter.setBrush(QColor(0, 100, 255, 100))
            for handle, rect in self.handles.items():
                if self.handleSelected is None or handle == self.handleSelected:
                    painter.drawEllipse(rect)

class LabelingView(QGraphicsView):
    def __init__(self, parent=None):
        super(LabelingView, self).__init__(parent)
        self.drawing_start = QPointF()
        self.current_rect_item = None
        self.is_drawing = False

    def mousePressEvent(self, event):
        if self.is_drawing:
            self.drawing_start = self.mapToScene(event.position().toPoint())
            self.current_rect_item = ResizableRectItem()
            self.current_rect_item.setFlag(QGraphicsRectItem.ItemIsMovable)
            self.current_rect_item.setFlag(QGraphicsRectItem.ItemIsSelectable)
            self.current_rect_item.setFlag(QGraphicsRectItem.ItemSendsGeometryChanges)
            self.current_rect_item.setAcceptHoverEvents(True)
            self.scene().addItem(self.current_rect_item)
        else:
            super(LabelingView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.is_drawing and self.current_rect_item:
            end_point = self.mapToScene(event.position().toPoint())
            rect = QRectF(self.drawing_start, end_point).normalized()
            self.current_rect_item.setRect(rect)
        else:
            super(LabelingView, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.is_drawing:
            self.is_drawing = False
            self.current_rect_item.updateHandlesPos()
            self.current_rect_item = None
        else:
            super(LabelingView, self).mouseReleaseEvent(event)

class LabelingTool(QWidget):
    def __init__(self, image_path, bbox_file_path):
        super(LabelingTool, self).__init__()

        self.image_path = image_path
        with open(bbox_file_path, 'r') as f:
            content = f.read()
            content = content.replace("'", '"')  # 작은따옴표를 큰따옴표로 변환
            self.bbox_coordinates = json.loads(content)

        self.scene = QGraphicsScene(self)
        self.view = LabelingView(self.scene)
        self.view.setMouseTracking(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.view)

        self.loadImageAndBBoxes()

        self.draw_button = QPushButton("Draw", self)
        self.draw_button.setCheckable(True)
        self.draw_button.clicked.connect(self.toggleDrawingMode)
        layout.addWidget(self.draw_button)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.deleteSelectedBBox)
        layout.addWidget(self.delete_button)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.saveBBoxes)
        layout.addWidget(self.save_button)

    def loadImageAndBBoxes(self):
        pixmap = QPixmap(self.image_path)
        pixmap_item = self.scene.addPixmap(pixmap)
        self.view.setScene(self.scene)

        for bbox_dict in self.bbox_coordinates:
            bbox = bbox_dict['bbox']
            rect = QRectF(bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1])
            bbox_item = ResizableRectItem(rect)
            self.scene.addItem(bbox_item)

    def toggleDrawingMode(self):
        self.view.is_drawing = not self.view.is_drawing

    def deleteSelectedBBox(self):
        for item in self.scene.selectedItems():
            self.scene.removeItem(item)

    def saveBBoxes(self):
        bboxes = []
        for item in self.scene.items():
            if isinstance(item, ResizableRectItem):
                rect = item.rect()
                bbox = [rect.left(), rect.top(), rect.right(), rect.bottom()]
                bboxes.append({'bbox': bbox})

        base_name = os.path.basename(self.image_path)
        file_name, _ = os.path.splitext(base_name)

        # 'app/gui/SampleRepo/원본이미지명' 디렉토리에 txt 파일을 저장
        dir_path = os.path.join('app', 'gui', 'SampleRepo', file_name)
        os.makedirs(dir_path, exist_ok=True)  # 디렉토리가 없으면 생성하고, 이미 있다면 그대로 둡니다.
        save_path = os.path.join(dir_path, f'{file_name}_privacy_bbox.txt')

        with open(save_path, 'w') as f:
            f.write("[\n")
            for i, bbox in enumerate(bboxes):
                if i != len(bboxes) - 1:
                    f.write(str(bbox) + ',\n')
                else:
                    f.write(str(bbox) + '\n')
            f.write("]\n")
def main():
    app = QApplication([])
    window = LabelingTool()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()