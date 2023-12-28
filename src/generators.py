from transformers import pipeline


def generate_intro(topic: str) -> dict[str, str]:
    input_text = f"Придумай введение (общую информацию и актуальность) к моей курсовой научно-исследовательской работе по теме {topic}"

    generator = pipeline('text-generation', model='ai-forever/rugpt3small_based_on_gpt2')
    gen_config = {
            "max_length": 430,
            "min_length": 210,
            "temperature": 1.1,
            "top_p": 2,
            "num_beams": 11,
            "repetition_penalty": 1.2,
            "num_return_sequences": 3,
            "no_repeat_ngram_size": 2,
            "do_sample": True
        }
    text = generator(input_text, pad_token_id=50256, **gen_config)
    return {'generated_text': text}


def generate_annotation(topic: str) -> dict[str, str]:
    input_text = f"Придумай общую аннотацию к моей курсовой научно-исследовательской работе по теме {topic}"

    generator = pipeline('text-generation', model='ai-forever/rugpt3small_based_on_gpt2')
    gen_config = {
            "max_length": 100,
            "min_length": 150,
            "temperature": 1.1,
            "top_p": 2,
            "num_beams": 10,
            "repetition_penalty": 1.2,
            "num_return_sequences": 4,
            "no_repeat_ngram_size": 2,
            "do_sample": True
        }
    text = generator(input_text, pad_token_id=50256, **gen_config)
    return {'generated_text': text[0]}