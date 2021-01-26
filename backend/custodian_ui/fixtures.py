from custodian_ui.policy.models import Policy, CloudProvider

 

def generate():

    f = open('fixtures/aws1.yml').read()
    aws1 = Policy(
      cloud=CloudProvider(CloudProvider("Amazon Web Services")),
      name="Account - Login from Invalid IP Address",
      description="""This policy will automatically create a CloudWatch Event Rule triggered Lambda function in your account and region which will be triggered anytime a user logs in from an invalid IP address.""",
      yaml=f,
    )
    aws1.save()

    f = open('fixtures/aws2.yml').read()
    aws2 = Policy(
      cloud=CloudProvider("Amazon Web Services"),
      name="Account - Detect Root Logins",
      description="""This policy will automatically create a CloudWatch Event Rule triggered Lambda function in your account and region which will be triggered anytime the root user of the account logs in.""",
      yaml=f,
    )
    aws2.save()

    f = open('fixtures/aws3.yml').read()
    aws3 = Policy(
      cloud=CloudProvider("Amazon Web Services"),
      name="Account Service Limit",
      description="""This policy will find any service in your region that is using more than 50% of the limit and raise the limit for 25%. """,
      yaml=f,
    )
    aws3.save()

    f = open('fixtures/aws4.yml').read()
    aws4 = Policy(
      cloud=CloudProvider("Amazon Web Services"),
      name="AMI - Stop EC2 using Unapproved AMIs",
      description="""This policy will stop Ec2 from using unapproved AMIs""", 
      yaml=f,
    )
    aws4.save()


    f = open('fixtures/aws5.yml').read()
    aws5 = Policy(
      cloud=CloudProvider("Amazon Web Services"),
      name="AutoScaling Group - Verify ASGs have valid configurations",
      description="""This policy will check all AutoScaling Groups in the current account and region for configuration issues which could prevent the ASG from functioning properly or launching an instance.""", 
      yaml=f,
    ) 
    aws5.save()
