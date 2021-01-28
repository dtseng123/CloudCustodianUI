from custodian_ui.policy.models import Policy, CloudProvider

 

def generate(cloud='aws'):

    if cloud == "aws":
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

    elif cloud == "gcloud":

      f = open('fixtures/gcp1.yml').read()
      gcp1 = Policy(
        cloud=CloudProvider("Google Cloud Platform"),
        name="App Engine - Check if an SSL Certificate is about to expire",
        description="""Custodian can check and notify if an SSL certificate is about to expire. Note that the notify action requires a Pub/Sub topic to be configured.""",
        yaml=f
      ) 

      f = open('fixtures/gcp2.yml').read()
      gcp2 = Policy(
        cloud=CloudProvider("Google Cloud Platform"),
        name="App Engine - Check if blacklisted domain is still in use",
        description="""Custodian can check and notify if there are user-defined blacklisted domains in use. Note that the notify action requires a Pub/Sub topic to be configured.""",
        yaml=f
      )

      f = open('fixtures/gcp3.yml').read()
      gcp3 = Policy(
        cloud=CloudProvider("Google Cloud Platform"),
        name="App Engine - Check if a Firewall Rule is in Place", 
        description="""Custodian can check and notify if App Engine firewall ingress rules have been misconfigured. Note that the notify action requires a Pub/Sub topic to be configured.""",
        yaml=f
      )

      f = open('fixtures/gcp4.yml').read()
      gcp4 = Policy(
        cloud=CloudProvider("Google Cloud Platform"),
        name="Dataflow - Check for Hanged Jobs",
        description="""Once started, a job in the Cloud Dataflow service transits from state to state and normally enters a terminal state. Custodian can check if there are any jobs hanging in temporary statuses abnormally long.""",
        yaml=f
      )

      f = open('fixtures/gcp5.yml').read()
      gcp5 = Policy(
        cloud=CloudProvider("Google Cloud Platform"),
        name="Deployment Manager - Find expired deployments",
        description="""Custodian can check and delete deployments that have reached their expiration date which is in turn determined by your governance rules.""",
        yaml=f
      )


    elif cloud == 'azure':
      
      f = open('fixtures/azu1.yml').read()
      azu1 = Policy(
        cloud=CloudProvider("Microsoft Azure Cloud"),
        name="Monitor - Filter resources by metrics from Azure Monitor 1",
        description="""Find VMs with an average Percentage CPU greater than or equal to 75% over the last 12 hours.""",
        yaml=f
      )

      f = open('fixtures/azu2.yml').read()
      azu2 = Policy(
        cloud=CloudProvider("Microsoft Azure Cloud"),
        name="Monitor - Filter resources by metrics from Azure Monitor 2",
        description="""Find KeyVaults with more than 1000 API hits in the last hour.""",
        yaml=f
      )

      f = open('fixtures/azu3.yml').read()
      azu3 = Policy(
        cloud=CloudProvider("Microsoft Azure Cloud"),
        name="Monitor - Filter resources by metrics from Azure Monitor 3",
        description="""Find SQL servers with less than 10% average DTU consumption over last 24 hours.""",
        yaml=f
      )

      f = open('fixtures/azu4.yml').read()
      azu4 = Policy(
        cloud=CloudProvider("Microsoft Azure Cloud"),
        name="Resource Groups - Delayed operations",
        description="""You can use the mark-for-op action and the marked-for-op filter to implement delayed actions, such as delete a resource if it remains non-compliant for a few days.""",
        yaml=f
      )

      f = open('fixtures/azu5.yml').read()
      azu5 = Policy(
        cloud=CloudProvider("Microsoft Azure Cloud"),
        name="Resource Groups - Remove empty Resource Groups",
        description="""Removes all empty resource groups from the subscription: """,
        yaml=f
      )