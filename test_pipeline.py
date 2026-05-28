from backend.core.orchestrator import Orchestrator

"""
UNIFIED TEST SCRIPT.
Now uses the Orchestrator to run all registered analyzers.
"""

def test_unified_pipeline():
    target = "tests/sample_vulnerable.sol"
    print(f"--- [Unified Pipeline] Starting Analysis on {target} ---")
    
    # 1. Initialize the "Project Manager" (Orchestrator)
    orchestrator = Orchestrator()
    
    # 2. Run the analysis (This handles all tools automatically)
    all_results = orchestrator.run_analysis(target)
    
    # 3. Report the findings from all tools
    total_findings = 0
    print("\n" + "="*50)
    print("FINAL CONSOLIDATED REPORT")
    print("="*50)
    
    for finding_set in all_results:
        # Each finding_set comes from a different tool
        tool_name = "Unknown Tool"
        if finding_set.findings:
            tool_name = finding_set.findings[0].tool
        
        print(f"\n>>> Results from {tool_name}:")
        print(f"Findings: {len(finding_set.findings)}")
        total_findings += len(finding_set.findings)
        
        for i, finding in enumerate(finding_set.findings, 1):
            print(f"  {i}. [{finding.severity}] {finding.title}")
            print(f"     Description: {finding.description[:80]}...")
            
    print("\n" + "="*50)
    print(f"ANALYSIS SUMMARY: Found {total_findings} total findings across {len(all_results)} tool(s).")
    print("="*50)

if __name__ == "__main__":
    test_unified_pipeline()
