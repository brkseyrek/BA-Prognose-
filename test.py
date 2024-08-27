from diagrams import Diagram, Edge
from diagrams.generic.network import Router, Switch, Firewall

with Diagram("User Prediction Process", show=False):
    start = Router("User Request")
    
    process_request = Switch("Process Request")
    
    user_data_gateway = Firewall("User Data Available?")
    
    send_request = Switch("Send Request to GPT-4o")
    
    receive_response = Switch("Receive Response from GPT-4o")
    
    db_query_gateway = Firewall("Database Query Required?")
    
    query_data = Switch("Query Data")
    
    analyze_data = Switch("Analyze and Combine Data")
    
    format_result = Switch("Format Result")
    
    end = Router("Display Result")
    
    start >> process_request >> user_data_gateway >> send_request >> receive_response >> db_query_gateway
    
    db_query_gateway >> Edge(label="Yes") >> query_data >> analyze_data >> format_result >> end
    db_query_gateway >> Edge(label="No") >> format_result >> end
