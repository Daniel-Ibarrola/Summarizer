import json


class TestCreateSummary:

    def test_create_summary(self, test_app_with_db):
        response = test_app_with_db.post(
            "/summaries/", data=json.dumps({"url": "https://foo.bar"}))
        assert response.status_code == 201
        assert response.json()["url"] == "https://foo.bar"

    def test_create_summary_invalid_json(self, test_app):
        response = test_app.post("/summaries/", data=json.dumps({}))
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "loc": ["body", "url"],
                    "msg": "field required",
                    "type": "value_error.missing"
                }
            ]
        }


class TestReadSummary:

    def test_read_summary(self, test_app_with_db):
        response = test_app_with_db.post(
            "/summaries/", data=json.dumps({"url": "https://foo.bar"}))
        summary_id = response.json()["id"]

        response = test_app_with_db.get(f"/summaries/{summary_id}/")
        assert response.status_code == 200

        response_dict = response.json()
        assert response_dict["id"] == summary_id
        assert response_dict["url"] == "https://foo.bar"
        assert response_dict["summary"]
        assert response_dict["created_at"]

    def test_read_summary_incorrect_id(self, test_app_with_db):
        response = test_app_with_db.get(f"/summaries/666/")
        assert response.status_code == 404
        assert response.json()["detail"] == "Summary not found"


class TestReadAllSummaries:

    def test_read_all_summaries(self, test_app_with_db):
        response = test_app_with_db.post(
            "/summaries/", data=json.dumps({"url": "https://foo.bar"}))
        summary_id = response.json()["id"]

        response = test_app_with_db.get("/summaries/")
        assert response.status_code == 200

        response_list = response.json()
        assert len(list(filter(lambda d: d["id"] == summary_id, response_list)))
