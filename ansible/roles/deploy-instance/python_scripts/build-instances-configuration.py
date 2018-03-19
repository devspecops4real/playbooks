instances_configuration = []

for host in hosts:
    host_copy = defaults.copy()

    host_copy.update(host)
    instances_configuration.append(host_copy)
