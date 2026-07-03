from dos_plugin_quantum import quantum_risk_advisor


def test_quantum_risk_is_advisory_only():
    assert quantum_risk_advisor({"data_labels": ["long_term_secret"]}) == "suspicious"
    assert quantum_risk_advisor({"data_labels": []}) is None
