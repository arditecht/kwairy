### ---------------------------------------------- ############################
# | SETTINGS TO DETERMINE GLOBAL RUNTIME BEHAVIOUR |			      		  #
###############################################################################


# | NOTE: Precision mode is by-default TRUE while development phase	          #

runtime = {
    "precision_mode" : True, # uses open ai model for inference, use false for cost savings mode
    "local_embed" : False, # Local embeddings are good enough and free to use, or if False, use open ai embeddings
    "memory" : "memory" # folder to store documents, stores, DBs, etc.
}

dev = {
    "debug_mode" : True, # use this to enable debug mode
    
}