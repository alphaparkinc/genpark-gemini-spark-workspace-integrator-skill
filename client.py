class GeminiSparkWorkspaceIntegratorClient:
    def integrate(self, doc_title: str, recipients: list[str]) -> dict:
        return {"operation_status": f"Sent {doc_title} draft to {recipients}"}