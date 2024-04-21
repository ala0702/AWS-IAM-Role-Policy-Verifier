# verifying the input JSON data

This project contains a method for verifying the input JSON data, specifically formatted as an AWS::IAM::Role Policy. The method checks if the input JSON data contains a single asterisk (\*) in the "Resource" field of any statement. If such a single asterisk is found in any of the 'Resource' fields, the method returns False, otherwise, it returns True.

## Usage

### Prerequisites

- Python 3.x

## How to Run

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ala0702/AWS-IAM-Role-Policy-Verifier.git
    ```
    
    

2. Navigate to the project directory:

    ```bash
    cd AWS-IAM-Role-Policy-Verifier
    ```

3. Run the program with the following command, providing the path to the JSON file as an argument:

    ```bash
    python HomeExercise.py <file_path>
    ```

    Replace `<file_path>` with the path to your JSON file.

## Input JSON Format

The input JSON data should be formatted according to the AWS IAM Role Policy format. Here's an example:

```json
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```
For more visit [my Profile](https://github.com/ala0702)
