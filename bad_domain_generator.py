import pandas as pd
import random


def generate_bad_domain(base_domain):
    variations = [
        lambda s: s[:-1] + '0' + s[-1] if s[-1].isdigit() else s + '0', 
        lambda s: s + '+1',
        lambda s: s + '1',
        lambda s: s + '2',
    ]

    random_variation = random.choice(variations)
    random_tld = random.choice(['.com', '.net', '.org', '.io', '.co'])
    base_part, tld_part = base_domain.rsplit('.', 1)

    return random_variation(base_part) + random_tld

good_domains_df = pd.read_csv('good_domains_202402131608.csv')
bad_domains = {'bad_domain': []}

for good_domain in good_domains_df['good_domain_names']:
    for _ in range(5):
        bad_domains['bad_domain'].append(generate_bad_domain(good_domain))

bad_domains_df = pd.DataFrame(bad_domains)
bad_domains_df.to_csv('bad_domains.csv', index=False)
