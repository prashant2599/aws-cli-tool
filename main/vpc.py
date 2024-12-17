import boto3

def list_vpc(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    vpcs = ec2.describe_vpcs()
    vpc_info = []

    for vpc in vpcs['Vpcs']:
        vpc_id = vpc['VpcId']
        vpc_cidr_block = vpc['CidrBlock']
        vpc_state = vpc['State']
        vpc_info.append({'VPC_ID': vpc_id, 'VPC_CIDR_BLOCK': vpc_cidr_block, 'VPC_STATE': vpc_state})

    return vpc_info

region = input("Enter the AWS region (e.g., us-east-1): ").strip()

try:
    vpcs = list_vpc(region)

    if vpcs:
        print(f"\nVPCs in region '{region}':")
        print("| #  | VPC ID                         | VPC CIDR BLOCK                 | VPC STATE   |")
        print("|----|---------------------------------|---------------------------------|-------------|")
        for index, vpc in enumerate(vpcs, start=1):
            print(f"| {index:<2} | {vpc['VPC_ID']:<30} | {vpc['VPC_CIDR_BLOCK']:<30} | {vpc['VPC_STATE']:<11} |")
        print("|----|---------------------------------|---------------------------------|-------------|")
    else:
        print(f"No VPCs found in region '{region}'.")
except Exception as e:
    print(f"Error fetching VPCs for region '{region}': {e}")
