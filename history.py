class OperationHistory:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def execute_operation(self, operation):
        operation.execute()
        self._undo_stack.append(operation)
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            raise ValueError("Nothing to undo.")
        operation = self._undo_stack.pop()
        operation.undo()
        self._redo_stack.append(operation)

    def redo(self):
        if not self._redo_stack:
            raise ValueError("Nothing to redo.")
        operation = self._redo_stack.pop()
        operation.execute()
        self._undo_stack.append(operation)