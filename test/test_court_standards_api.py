from unicourt.sdk.CourtStandards import CourtStandards


class TestCourtStandards:
    def test_get_appeal_courts_for_court():
        return CourtStandards.get_appeal_courts_for_court(
            court_id='CORThSxcef8eGUSkuC'
        )

    def test_get_area_of_law():
        return CourtStandards.get_area_of_law(
            area_of_law_id='AOFLGAd9Ah5qkTRNw9'
        )

    def test_get_areas_of_law():
        return CourtStandards.get_areas_of_law(
            q='areaOfLawId: "AOFLGAd9Ah5qkTRNw9"'
        )

    def test_get_attorney_representation_type():
        return CourtStandards.get_attorney_representation_type(
            attorney_representation_type_id='ATRPYgPMGJufoCsR6Q'
        )

    def test_get_attorney_representation_types():
        return CourtStandards.get_attorney_representation_types(
            q='attorneyRepresentationTypeId: "ATRPYgPMGJufoCsR6Q"'
        )

    def test_get_attorney_type():
        return CourtStandards.get_attorney_type(
            attorney_type_id='ATYPWXtARwvzu5HLcf',
        )

    def test_get_attorney_types():
        return CourtStandards.get_attorney_types(
            q='attorneyTypeId:"ATYPWXtARwvzu5HLcf"'
        )

    def test_get_case_class():
        return CourtStandards.get_case_class(
            case_class_id='CSCLNjbKTN7Yfo2wdb',
        )

    def test_get_case_relationship_type():
        return CourtStandards.get_case_relationship_type(
            case_relationship_type_id='CRTPgkmnzpiBXstT3s',
        )

    def test_get_case_relationship_types():
        return CourtStandards.get_case_relationship_types(
            q='caseRelationshipTypeId: "CRTPgkmnzpiBXstT3s"'
        )

    def test_get_case_status():
        return CourtStandards.get_case_status(
            case_status_id='CSSTBtqf3R2LYFt4j4',
        )

    def test_get_case_status_group():
        return CourtStandards.get_case_status_group(
            case_status_group_id='CSSG6ERqyFdydo52WK',
        )

    def test_get_case_status_groups():
        return CourtStandards.get_case_status_groups(
            q='caseStatusGroupId:"CSSG6ERqyFdydo52WK"'
        )

    def test_get_case_type():
        return CourtStandards.get_case_type(
            case_type_id='CTYPoLU7sWaGjWtkBx',
        )

    def test_get_case_type_group():
        return CourtStandards.get_case_type_group(
            case_type_group_id='CTYGSpWaVityBQndsv',
        )

    def test_get_case_type_groups():
        return CourtStandards.get_case_type_groups(
            q='caseTypeGroupId: "CTYGSpWaVityBQndsv"'
        )

    def test_get_case_types():
        return CourtStandards.get_case_types(
            q='caseTypeId: "CTYPoLU7sWaGjWtkBx"'
        )

    def test_get_cases_class():
        return CourtStandards.get_cases_class(
            q='caseClassId:"CSCLNjbKTN7Yfo2wdb"'
        )

    def test_get_cases_status():
        return CourtStandards.get_cases_status(
            q='caseStatusId: "CSSTBtqf3R2LYFt4j4"'
        )

    def test_get_cause_of_action():
        return CourtStandards.get_cause_of_action(
            cause_of_action_id = 'CATNoLU7sWaGjWtkBx'
        )

    def test_get_cause_of_action_additional_data():
        return CourtStandards.get_cause_of_action_additional_data(
            cause_of_action_additional_data_id = 'CAADoLU7sWaGjWtkBx'
        )

    def test_get_cause_of_action_group():
        return CourtStandards.get_cause_of_action_group(
            cause_of_action_group_id = 'CAGPoLU7sWaGjWtkBx'
        )

    def test_get_causes_of_action():
        return CourtStandards.get_causes_of_action(
            q='causeOfActionGroupId:"CAGPiHoKn66p3bkcNs"'
        )

    def test_get_causes_of_action_additional_data():
        return CourtStandards.get_causes_of_action_additional_data(
            q='causeOfActionAdditionalDataId:"CAADiHoKn66p3bkcNs"'
        )

    def test_get_causes_of_action_group():
        return CourtStandards.get_causes_of_action_group(
            q='causeOfActionGroupId:"CAGPiHoKn66p3bkcNs"'
        )

    def test_get_charge():
        return CourtStandards.get_charge(
            charge_id = 'CHRGiHoKn66p3bkcNs'
        )

    def test_get_charge_additional_data():
        return CourtStandards.get_charge_additional_data(
            charge_additional_data_id = 'CHADiHoKn66p3bkcNs'
        )

    def test_get_charge_degree():
        return CourtStandards.get_charge_degree(
            charge_degree_id = 'CHDGiHoKn66p3bkcNs'
        )

    def test_get_charge_group():
        return CourtStandards.get_charge_group(
            charge_group_id = 'CHGPiHoKn66p3bkcNs'
        )

    def test_get_charge_groups():
        return CourtStandards.get_charge_groups(
            q = 'chargeGroupId:"CHRGoLU7sWaGjWtkBx"'
        )

    def test_get_charge_severity():
        return CourtStandards.get_charge_severity(
            charge_severity_id = 'CHSEiHoKn66p3bkcNs'
        )

    def test_get_charges():
        return CourtStandards.get_charges(
            q='chargeId:"CHRGoLU7sWaGjWtkBx"'
        )

    def test_get_charges_additional_data():
        return CourtStandards.get_charges_additional_data(
            q = 'chargeAdditionalDataId:"CHADoLU7sWaGjWtkBx"'
        )

    def test_get_charges_degree():
        return CourtStandards.get_charges_degree(
            q = 'chargeDegreeId:"CHDGiHoKn66p3bkcNs"'
        )

    def test_get_charges_severity():
        return CourtStandards.get_charges_severity(
            q = 'chargeSeverityId:"CHSEiHoKn66p3bkcNs"'
        )

    def test_get_court():
        return CourtStandards.get_court(
            court_id='CORThSxcef8eGUSkuC'
        )

    def test_get_court_location():
        return CourtStandards.get_court_location(
            court_location_id="COLO9g3fhYM4bmxveA"
        )

    def test_get_court_locations():
        return CourtStandards.get_court_locations()

    def test_get_court_locations_for_court():
        return CourtStandards.get_court_locations_for_court(
            court_id="CORThSxcef8eGUSkuC"
        )

    def test_get_court_service_status():
        return CourtStandards.get_court_service_status(
            court_service_status_id="CTSSf45fd1bd792e97"
        )

    def test_get_court_system():
        return CourtStandards.get_court_system(
            court_system_id='COSY4vuCtGQeAmdDdN'
        )

    def test_get_court_systems():
        return CourtStandards.get_court_systems(
            q='courtSystemId:"COSY4vuCtGQeAmdDdN"'
        )

    def test_get_court_type():
        return CourtStandards.get_court_type(
            court_type_id='COTPm8jjc2PAydpFhq'
        )

    def test_get_court_types():
        return CourtStandards.get_court_types(
            q='courtTypeId:"COTPm8jjc2PAydpFhq"'
        )

    def test_get_courts():
        return CourtStandards.get_courts(
            q='courtId:"CORThSxcef8eGUSkuC"'
        )

    def test_get_courts_for_court_location():
        return CourtStandards.get_courts_for_court_location(
            court_location_id='COLOV75AKgqMqnfVhM'
        )

    def test_get_courts_for_jurisdiction_geo():
        return CourtStandards.get_courts_for_jurisdiction_geo(
            jurisdiction_geo_id='JUGO8s7HvM84dLvVMu'
        )

    def test_get_courts_service_status():
        return CourtStandards.get_courts_service_status(
            q='courtServiceStatusId: "CTSSf45fd1bd792e97"'
        )

    def test_get_judge_type():
        return CourtStandards.get_judge_type(
            judge_type_id='JGTPkwrfzkDJUvxpN9'

        )

    def test_get_judge_types():
        return CourtStandards.get_judge_types(
            q='judgeTypeId: "JGTPkwrfzkDJUvxpN9"'
        )

    def test_get_jurisdiction_geo():
        return CourtStandards.get_jurisdiction_geo(
            jurisdiction_geo_id='JUGO8s7HvM84dLvVMu'
        )

    def test_get_jurisdiction_geo_for_court():
        return CourtStandards.get_jurisdiction_geo_for_court(
            court_id='CORThSxcef8eGUSkuC'
        )

    def test_get_jurisdictions_geo():
        return CourtStandards.get_jurisdictions_geo(
            q='jurisdictionGeoId:"JUGO8s7HvM84dLvVMu"'
        )

    def test_get_party_role():
        return CourtStandards.get_party_role(
            party_role_id='PTYRVRgMKueGmhnxRN'
        )

    def test_get_party_role_group():
        return CourtStandards.get_party_role_group(
            party_role_group_id='PTYGBnjxbx6tKNfVEP'
        )

    def test_get_party_role_groups():
        return CourtStandards.get_party_role_groups(
            q='partyRoleGroupId: "PTYGBnjxbx6tKNfVEP"'
        )

    def test_get_party_roles():
        return CourtStandards.get_party_roles(
            q='partyRoleId: "PTYRVRgMKueGmhnxRN"'
        )
