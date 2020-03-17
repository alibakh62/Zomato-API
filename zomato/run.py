import sys
sys.path.insert(0, '.')
sys.path.insert(0, '..')

import os
from zomatoapi import Zomato
import pandas as pd
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Zomato Arg Parser')

parser.add_argument('--key', type=str, help="API key", required=True)
parser.add_argument('--input', type=str, help="input file", required=True)
parser.add_argument('--output', type=str, help="output folder", required=True)
parser.add_argument('--states', nargs="*", help="select specific US states")

args = parser.parse_args()

def main(args):
    states = args.states
    INPUT = args.input
    OUTPUT_DIR = args.output
    z = Zomato(args.key)
    inputdf = pd.read_csv(INPUT)
    inputdf.columns = map(str.lower, inputdf.columns)
    if states:
        inputdf = inputdf.loc[inputdf["state"].isin(states),] 
    print(f"inputdf size: {inputdf.shape}")
    rest_info = []
    cnt = 1
    for _, row in inputdf.iterrows():
        response = z.search(row['city'], row['latitude'], row['longitude'])
        try:
            if response != "null":
                print(f"Count: {cnt}")
                print(f"results found: {response['results_found']}")
                print(f"results shown: {response['results_shown']}")
                restaurants = response['restaurants']
            
                for restaurant in restaurants:
                    rest = {}
                    rest.update({'id' : restaurant['restaurant']['id']})
                    rest.update({'name':restaurant['restaurant']['name']})
                    rest.update({'address':restaurant['restaurant']['location']['address']})
                    rest.update({'locality':restaurant['restaurant']['location']['locality']})
                    rest.update({'locality_verbose':restaurant['restaurant']['location']['locality_verbose']})
                    rest.update({'city':restaurant['restaurant']['location']['city']})
                    rest.update({'city_id':restaurant['restaurant']['location']['city_id']})
                    rest.update({'latitude':restaurant['restaurant']['location']['latitude']})
                    rest.update({'longitude':restaurant['restaurant']['location']['longitude']})
                    rest.update({'zipcode':restaurant['restaurant']['location']['zipcode']})
                    rest.update({'cuisines':restaurant['restaurant']['cuisines']})
                    rest.update({'timings':restaurant['restaurant']['timings']})
                    rest.update({'average_cost_for_two':restaurant['restaurant']['average_cost_for_two']})
                    rest.update({'price_range':restaurant['restaurant']['price_range']})
                    rest.update({'highlights':restaurant['restaurant']['highlights']})
                    rest.update({'opentable_support':restaurant['restaurant']['opentable_support']})
                    rest.update({'aggregate_rating':restaurant['restaurant']['user_rating']['aggregate_rating']})
                    rest.update({'rating_text':restaurant['restaurant']['user_rating']['rating_text']})
                    rest.update({'votes':restaurant['restaurant']['user_rating']['votes']})
                    rest.update({'all_reviews_count':restaurant['restaurant']['all_reviews_count']})
                    rest.update({'photo_count':restaurant['restaurant']['photo_count']})
                    rest.update({'has_online_delivery':restaurant['restaurant']['has_online_delivery']})
                    rest.update({'is_delivering_now':restaurant['restaurant']['is_delivering_now']})
                    rest_info.append(rest)
        except KeyError:
            pass
        cnt += 1
        print("="*50)
            
    df = pd.DataFrame(rest_info)
    states_v= "_".join(states)
    time_v = datetime.now().strftime(format="%Y%m%d_%H%M%S")
    df.to_csv(os.path.join(OUTPUT_DIR, f"restaurants_{states_v}_{time_v}.csv"), index=False)


if __name__ == "__main__":
    main(args)
        



