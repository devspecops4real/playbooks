import json

inventory_configuration = []
ip_addresses = []

for ec2_instance in ec2_instances['results']:
    row = {}

    row['item'] = ec2_instance['item']
    row['results'] = json.load(open(ec2_instance['results_file']))

    for tagged_instance in row['results']['tagged_instances']:
        ip_addresses.append(tagged_instance['private_ip'])

    inventory_configuration.append(row)
