from unicourt.sdk.JudgeAnalytics import JudgeAnalytics


class TestJudgeAnalytics:
    def test_get_norm_attorneys_associated_with_norm_judge():
        return JudgeAnalytics.get_norm_attorneys_associated_with_norm_judge(
            norm_judge_id='NJUDT7jCZyFNeLGpRq',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_judge_by_id():
        return JudgeAnalytics.get_norm_judge_by_id(
            norm_judge_id='NJUDT7jCZyFNeLGpRq'
        )

    def test_get_norm_law_firms_associated_with_norm_judge():
        return JudgeAnalytics.get_norm_law_firms_associated_with_norm_judge(
            norm_judge_id='NJUDT7jCZyFNeLGpRq',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_parties_associated_with_norm_judge():
        return JudgeAnalytics.get_norm_parties_associated_with_norm_judge(
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]',
            norm_judge_id='NJUDT7jCZyFNeLGpRq',
            page_number=1
        )

    def test_search_normalized_judges():
        return JudgeAnalytics. search_normalized_judges(
            q='normJudgeId:"NJUD5STmDbUZGukfQm"'
        )

    def test_search_normalized_judges_by_id():
        return JudgeAnalytics. search_normalized_judges_by_id(
            norm_judge_search_id='JSRCNUSK3pLGe48QcU'
        )
