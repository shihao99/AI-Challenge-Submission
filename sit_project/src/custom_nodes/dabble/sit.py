from typing import Any, Dict, List, Tuple
import cv2
from peekingduck.pipeline.nodes.abstract_node import AbstractNode


# setup global constants
FONT = cv2.FONT_HERSHEY_SIMPLEX
WHITE = (255, 255, 255)  # opencv loads file in BGR format
YELLOW = (0, 255, 255)


class Node(AbstractNode):
    def __init__(self, config: Dict[str, Any] = None, **kwargs: Any) -> None:
        super().__init__(config, node_path=__name__, **kwargs)
        # setup object working variables
        self.is_sit = False
        self.num_sitting = 0

    def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        # get required inputs from pipeline
        people = inputs['obj_attrs']

        # obj_attrs is a dictionary
        sitting = len(list(people.values())[0])

        print(f"There are currently {sitting} people sitting down.")

        return {}
