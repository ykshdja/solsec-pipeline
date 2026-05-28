from abc import ABC, abstractmethod
from .models import FindingSet

"""
DEFINE AN ABSTRACT BASE CLASS (ABC) THAT ALL ANALYZERS MUST FOLLOW.
THIS DEFINES THE run() METHOD THAT THE ORCHESTRATOR WILL CALL.
"""

class BaseAnalyzer(ABC):
    """
    Abstract Base Class for all security analyzers.
    Every tool wrapper (Slither, Mythril, etc.) must inherit from this.
    """

    def __init__(self, target_path: str):
        self.target_path = target_path

    """
    Executes the analysis tool and returns a standardized FindingSet.
    Must be implemented by all subclasses.
    """
    @abstractmethod
    def run(self) -> FindingSet:
        pass
