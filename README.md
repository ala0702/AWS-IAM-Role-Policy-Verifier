# verifying the input JSON data

This project contains a method for verifying the input JSON data, specifically formatted as an AWS::IAM::Role Policy. The method checks if the input JSON data contains a single asterisk (\*) in the "Resource" field of any statement. If such a single asterisk is found in any of the 'Resource' fields, the method returns False, otherwise, it returns True.

## Usage

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

git clone <repository-url>

### Running the Method

1. Ensure you have a JSON file containing an IAM Role Policy definition. The JSON file should adhere to the following format:

```json
{
  "PolicyName": "root",
  "PolicyDocument": {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "IamListAccess",
        "Effect": "Allow",
        "Action": ["iam:ListRoles", "iam:ListUsers"],
        "Resource": "*"
      }
    ]
  }
}

2. Invoke the verify_input method by passing the file path of your JSON file as an argument:

python HomeExercise.py <yourPathToFile.json>


The method will return True if there are no single asterisks (*) in the "Resource" field of any statement, and False otherwise.


```
