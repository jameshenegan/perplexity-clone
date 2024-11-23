import json

class Serializer:
    @staticmethod
    def serialize_to_json(chat_completion):
        """
        Serializes a ChatCompletion object to a JSON file.

        Args:
            chat_completion: The ChatCompletion object to serialize.
            file_path: The file path where the JSON should be saved.

        Returns:
            None
        """
        try:
            # Convert the ChatCompletion object to a dictionary
            response_dict = {
                "id": chat_completion.id,
                "choices": [
                    {
                        "finish_reason": choice.finish_reason,
                        "index": choice.index,
                        "logprobs": choice.logprobs,
                        "message": {
                            "content": choice.message.content,
                            "refusal": choice.message.refusal,
                            "role": choice.message.role,
                            "audio": choice.message.audio,
                            "function_call": choice.message.function_call,
                            "tool_calls": choice.message.tool_calls,
                        },
                    }
                    for choice in chat_completion.choices
                ],
                "created": chat_completion.created,
                "model": chat_completion.model,
                "object": chat_completion.object,
                "service_tier": chat_completion.service_tier,
                "system_fingerprint": chat_completion.system_fingerprint,
                "usage": {
                    "completion_tokens": chat_completion.usage.completion_tokens,
                    "prompt_tokens": chat_completion.usage.prompt_tokens,
                    "total_tokens": chat_completion.usage.total_tokens,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": chat_completion.usage.completion_tokens_details.accepted_prediction_tokens,
                        "audio_tokens": chat_completion.usage.completion_tokens_details.audio_tokens,
                        "reasoning_tokens": chat_completion.usage.completion_tokens_details.reasoning_tokens,
                        "rejected_prediction_tokens": chat_completion.usage.completion_tokens_details.rejected_prediction_tokens,
                    },
                    "prompt_tokens_details": {
                        "audio_tokens": chat_completion.usage.prompt_tokens_details.audio_tokens,
                        "cached_tokens": chat_completion.usage.prompt_tokens_details.cached_tokens,
                    },
                },
            }

            
            return response_dict
        
        except Exception as e:
            print(f"An error occurred during serialization: {e}")

# Example usage
# Assuming `chat_completion` is your ChatCompletion object
# serializer = Serializer()
# serializer.serialize_to_json(chat_completion, "output.json")
