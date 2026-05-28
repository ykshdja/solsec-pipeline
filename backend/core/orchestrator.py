from typing import List
from .models import FindingSet
from ..plugins.slither_analyzer import SlitherAnalyzer

"""
=== ORCHESTRATOR ===
Initialize the plugins (Slither/Mythril/Solhint).
Trigger the Analysis.
This serves as the central hub for coordinating multiple analysis tools.
"""

class Orchestrator:
    def __init__(self):
        """
        Use a plugin loader here in the future.
        Right now, we manually register plugins.
        """
        self.analyzers = []

    """
    Coordinates the execution of all registered analyzers on a single file.
    Returns a list of FindingSet objects.
    """
    def run_analysis(self, file_path: str) -> List[FindingSet]:
        self.analyzers = [
            SlitherAnalyzer(file_path)
        ]
        
        all_results = []
        print(f"[Orchestrator] Starting analysis on: {file_path}")
        
        for analyzer in self.analyzers:
            print(f"[Orchestrator] Running {analyzer.__class__.__name__}...")
            result = analyzer.run()
            all_results.append(result)
            
        print(f"[Orchestrator] Analysis Complete. Collected {len(all_results)} result set(s).")
        return all_results
