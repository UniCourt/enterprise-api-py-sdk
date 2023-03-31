from unicourt.sdk.CaseSearch import CaseSearch


class TestCaseSearch:
    def test_search_cases():
        return CaseSearch.search_cases(
            q='caseNumber:"JP07-22-DC00026818"',
            sort='filedDate',
            order='desc',
            page_number=1
        )

    def test_search_cases_by_id():
        return CaseSearch.search_cases_by_id(
            case_search_id='CSRCU3qFUH8BjLnba5'
        )
