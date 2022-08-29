def lambda_handler(event, context):
    print("Hello World, from a Lambda Function 1! update 1")
    output_string = "Hello World, from a Lambda Function 1!, update 2"
    return output_string
