"""Fit the blend weights from the journal. Runs after a cycle, never inside one.

The one package here that both reads the journal and writes something the
trading cycle will read. It writes exactly one file, the weights artifact,
and it has no order path; CI checks both, and checks that the orchestrator
never imports it.
"""
