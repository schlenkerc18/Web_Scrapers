# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd

def send_request(page_number: int, offset_parameter: int):
    url = "https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta"
    headers = {"content-type": "application/json"}

    # Madison
    # body = r'{"query":"\n\nquery ConsumerSearchMainQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket)\n{\n  home_search: home_search(query: $query,\n    sort: $sort,\n    limit: $limit,\n    offset: $offset,\n    sort_type: $sort_type,\n    client_data: $client_data,\n    bucket: $bucket,\n  ){\n    count\n    total\n    results {\n      property_id\n      list_price\n      primary_photo (https: true){\n        href\n      }\n      source {\n        id\n        agents{\n          office_name\n        }\n        type\n        spec_id\n        plan_id\n      }\n      community {\n        property_id\n        description {\n          name\n        }\n        advertisers{\n          office{\n            hours\n            phones {\n              type\n              number\n            }\n          }\n          builder {\n            fulfillment_id\n          }\n        }\n      }\n      products {\n        brand_name\n        products\n      }\n      listing_id\n      matterport\n      virtual_tours{\n        href\n        type\n      }\n      status\n      permalink\n      price_reduced_amount\n      other_listings{rdc {\n      listing_id\n      status\n      listing_key\n      primary\n    }}\n      description{\n        beds\n        baths\n        baths_full\n        baths_half\n        baths_1qtr\n        baths_3qtr\n        garage\n        stories\n        type\n        sub_type\n        lot_sqft\n        sqft\n        year_built\n        sold_price\n        sold_date\n        name\n      }\n      location{\n        street_view_url\n        address{\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n          }\n        }\n        county {\n          name\n          fips_code\n        }\n      }\n      tax_record {\n        public_record_id\n      }\n      lead_attributes {\n        show_contact_an_agent\n        opcity_lead_attributes {\n          cashback_enabled\n          flip_the_market_enabled\n        }\n        lead_type\n        ready_connect_mortgage {\n          show_contact_a_lender\n          show_veterans_united\n        }\n      }\n      open_houses {\n        start_date\n        end_date\n        description\n        methods\n        time_zone\n        dst\n      }\n      flags{\n        is_coming_soon\n        is_pending\n        is_foreclosure\n        is_contingent\n        is_new_construction\n        is_new_listing (days: 14)\n        is_price_reduced (days: 30)\n        is_plan\n        is_subdivision\n      }\n      list_date\n      last_update_date\n      coming_soon_date\n      photos(limit: 2, https: true){\n        href\n      }\n      tags\n      branding {\n        type\n        photo\n        name\n      }\n    }\n  }\n}","variables":{"query":{"status":["for_sale","ready_to_build"],"primary":true,"search_location":{"location":"47250, Madison, IN"}},"client_data":{"device_data":{"device_type":"web"},"user_data":{"last_view_timestamp":-1}},"limit":42,"offset":0,"zohoQuery":{"silo":"search_result_page","location":"47250, Madison, IN","property_status":"for_sale","filters":{}},"sort_type":"relevant","geoSupportedSlug":"47250","bucket":{"sort":"modelF"},"by_prop_type":["home"]},"operationName":"ConsumerSearchMainQuery","callfrom":"SRP","nrQueryType":"MAIN_SRP","visitor_id":"f8f3952b-fb71-43f0-a01e-036eb8653509","isClient":true,"seoPayload":{"asPath":"/realestateandhomes-search/47250","pageType":{"silo":"search_result_page","status":"for_sale"},"county_needed_for_uniq":false}}'
    body = r'{"query":"\n\nquery ConsumerSearchMainQuery($query: HomeSearchCriteria!, $limit: Int, $offset: Int, $sort: [SearchAPISort], $sort_type: SearchSortType, $client_data: JSON, $bucket: SearchAPIBucket)\n{\n  home_search: home_search(query: $query,\n    sort: $sort,\n    limit: $limit,\n    offset: $offset,\n    sort_type: $sort_type,\n    client_data: $client_data,\n    bucket: $bucket,\n  ){\n    count\n    total\n    results {\n      property_id\n      list_price\n      primary_photo (https: true){\n        href\n      }\n      source {\n        id\n        agents{\n          office_name\n        }\n        type\n        spec_id\n        plan_id\n      }\n      community {\n        property_id\n        description {\n          name\n        }\n        advertisers{\n          office{\n            hours\n            phones {\n              type\n              number\n            }\n          }\n          builder {\n            fulfillment_id\n          }\n        }\n      }\n      products {\n        brand_name\n        products\n      }\n      listing_id\n      matterport\n      virtual_tours{\n        href\n        type\n      }\n      status\n      permalink\n      price_reduced_amount\n      other_listings{rdc {\n      listing_id\n      status\n      listing_key\n      primary\n    }}\n      description{\n        beds\n        baths\n        baths_full\n        baths_half\n        baths_1qtr\n        baths_3qtr\n        garage\n        stories\n        type\n        sub_type\n        lot_sqft\n        sqft\n        year_built\n        sold_price\n        sold_date\n        name\n      }\n      location{\n        street_view_url\n        address{\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n          }\n        }\n        county {\n          name\n          fips_code\n        }\n      }\n      tax_record {\n        public_record_id\n      }\n      lead_attributes {\n        show_contact_an_agent\n        opcity_lead_attributes {\n          cashback_enabled\n          flip_the_market_enabled\n        }\n        lead_type\n        ready_connect_mortgage {\n          show_contact_a_lender\n          show_veterans_united\n        }\n      }\n      open_houses {\n        start_date\n        end_date\n        description\n        methods\n        time_zone\n        dst\n      }\n      flags{\n        is_coming_soon\n        is_pending\n        is_foreclosure\n        is_contingent\n        is_new_construction\n        is_new_listing (days: 14)\n        is_price_reduced (days: 30)\n        is_plan\n        is_subdivision\n      }\n      list_date\n      last_update_date\n      coming_soon_date\n      photos(limit: 2, https: true){\n        href\n      }\n      tags\n      branding {\n        type\n        photo\n        name\n      }\n    }\n  }\n}","variables":{"query":{"status":["for_sale","ready_to_build"],"primary":true,"search_location":{"location":"Rahway, NJ"}},"client_data":{"device_data":{"device_type":"web"},"user_data":{"last_view_timestamp":-1}},"limit":42,"offset":0,"zohoQuery":{"silo":"search_result_page","location":"Rahway, NJ","property_status":"for_sale","filters":{}},"sort_type":"relevant","geoSupportedSlug":"Rahway_NJ","bucket":{"sort":"modelF"},"by_prop_type":["home"]},"operationName":"ConsumerSearchMainQuery","callfrom":"SRP","nrQueryType":"MAIN_SRP","user_id":"62e9ba447a6b5901cecfd37b","isClient":true,"seoPayload":{"asPath":"/realestateandhomes-search/Rahway_NJ","pageType":{"silo":"search_result_page","status":"for_sale"},"county_needed_for_uniq":false}}'
    json_body = json.loads(body)

    json_body["variables"]["page_index"] = page_number
    json_body["seoPayload"] = page_number
    json_body["variables"]["offset"] = offset_parameter

    r = requests.post(url=url, json=json_body, headers=headers)
    json_data = r.json()
    return json_data

offset_parameter = 0

json_data_list = []

for page_number in range(1, 3):
    json_data = send_request(page_number=page_number, offset_parameter=offset_parameter)
    json_data_list.append(json_data)
    offset_parameter +=42

def extract_features(entry: dict):
    feature_dict = {
        "id": entry["property_id"],
        "price": entry["list_price"],
        "beds": entry["description"]["beds"],
        "baths": entry["description"]["baths"],
        "garage": entry["description"]["garage"],
        "stories": entry["description"]["stories"],
        "house_type": entry["description"]["type"],
        "lot_sqft": entry["description"]["lot_sqft"],
        "sqft": entry["description"]["sqft"],
        "year_built": entry["description"]["year_built"],
        "address": entry["location"]["address"]["line"],
        "postal_code": entry["location"]["address"]["postal_code"],
        "state": entry["location"]["address"]["state_code"],
        "city": entry["location"]["address"]["city"],
        "tags": entry["tags"]
    }

    if entry["location"]["address"]["coordinate"]:
        feature_dict.update({"lat": entry["location"]["address"]["coordinate"]["lat"]})
        feature_dict.update({"lon": entry["location"]["address"]["coordinate"]["lon"]})
    if entry["location"]["county"]:
        feature_dict.update({"county": entry["location"]["county"]["name"]})

    return feature_dict

feature_dict_list = []

for data in json_data_list:
    for entry in data["data"]["home_search"]["results"]:
        feature_dict = extract_features(entry=entry)
        feature_dict_list.append(feature_dict)

df = pd.DataFrame(feature_dict_list)
dummy_df = pd.get_dummies(df['tags'].explode()).groupby(level=0).sum()
merged_df = pd.merge(df, dummy_df, left_index=True, right_index=True)

print(merged_df.head())
print(len(merged_df))
len(merged_df)

merged_df.to_csv(r'C:\Users\Schlenker18\PycharmProjects\RealtorScraper\rahway_real_estate.csv')