import settings

class LLMConfig () :
	def __init__(self) :
		is_pm = settings.runtime_logistics["performance_mode"]
		if is_pm : # This is by-default TRUE while development phase
			# gpt 3.5 and gpt 4 route

			pass
		else :
			# llama 2 route: install LlamaCPP to enable GPU efficient LLama-2 13B chat model to work acc to the production environment chosen.
			# download guide: https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast--metal
			# implementation guide: https://gpt-index.readthedocs.io/en/latest/examples/llm/llama_2_llama_cpp.html 
			'''
			from llama_index.llms import LlamaCPP
			from llama_index.llms.llama_utils import messages_to_prompt, completion_to_prompt

			llm = LlamaCPP(
				# You can pass in the URL to a GGML model to download it automatically
				model_url="https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/llama-2-13b-chat.ggmlv3.q4_0.bin",
				# optionally, you can set the path to a pre-downloaded model instead of model_url
				model_path=None,
				temperature=0.1,
				max_new_tokens=256,
				# llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
				context_window=3900,
				# kwargs to pass to __call__()
				generate_kwargs={},
				# kwargs to pass to __init__()
				# set to at least 1 to use GPU
				model_kwargs={"n_gpu_layers": 1},
				# transform inputs into Llama2 format
				messages_to_prompt=messages_to_prompt,
				completion_to_prompt=completion_to_prompt,
				verbose=True,
			)
			'''
			pass
             