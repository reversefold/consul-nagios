#!/usr/bin/env python
"""
Usage:
    consul-nagios.py <service> <CheckID> [--tag=<tag>]

"""
import sys

import consul
from docopt import docopt


EXITCODES = {
    'passing': 0,
    'warning': 1,
    'failing': 2,
    'critical': 3,
}


def main(service, check_id, tag=None):
    c = consul.Consul()
    index, nodes = c.health.service(service, tag=tag)
    for node in nodes:
        for check in node['Checks']:
            if check['CheckID'] == check_id:
                exit_code = EXITCODES[check['Status']]
                print check['Output']
                sys.exit(exit_code)

    print >>sys.stderr, 'Check with CheckID %r for service %r and tag %r not found' % (check_id, service, tag)
    sys.exit(1)


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args['<service>'], args['<CheckID>'], args['--tag'])
