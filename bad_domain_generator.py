import pandas as pd
import random


def extract_base_domain(good_domain):
    netloc_parts = good_domain.split('.')
    domain = netloc_parts[0]
    return domain

def jumble_last_three(s):
    if len(s) >= 3:
        last_three = list(s[-3:])
        random.shuffle(last_three)
        return s[:-3] + ''.join(last_three)
    else:
        return s

def generate_bad_domain(base_domain):
    variations = [
        lambda s: s[:-1] + '0' + s[-1] if s[-1].isdigit() else s + '0', 
        lambda s: s + '+1',
        lambda s: s + '1',
        lambda s: s + '2',
        lambda s: s.replace('o', '0').replace('l', '1'), 
        jumble_last_three
    ]

    random_variation = random.choice(variations)
    random_tld = random.choice(['.com', '.net', '.org', '.io', '.co'])

    return random_variation(base_domain) + random_tld

good_domains_df = pd.read_csv('good_domains_202402141950.csv')
bad_domains = {'bad_domain': []}

for good_domain in good_domains_df['good_domain_names']:
    base_domain = extract_base_domain(good_domain)
    for _ in range(1):
        bad_domains['bad_domain'].append(generate_bad_domain(base_domain))

bad_domains_df = pd.DataFrame(bad_domains)
print(bad_domains_df)
bad_domains_df.to_csv('bad_domains.csv', index=False)
