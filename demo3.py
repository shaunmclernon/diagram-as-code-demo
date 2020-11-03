from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.database import RDS
from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

with Diagram("Simple Website Diagram") as diag:
    dns = Route53("dns")
    load_balancer = ELB("Load Balancer")
    database = RDS("User Database")
    cache = Redis("Cache")
    with Cluster("Webserver Cluster"):
        svc_group = [EC2("Webserver 1"),
                    EC2("Webserver 2"),
                    EC2("Webserver 3")]
diag
