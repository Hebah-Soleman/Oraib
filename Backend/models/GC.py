from ibm_watsonx_ai.foundation_models import Model

class ArabicGrammarParser:
    def __init__(self, model_id, project_id, api_url, api_key):
        self.model_id = model_id
        self.project_id = project_id
        self.credentials = {
            "url": api_url,
            "apikey": api_key
        }
        self.parameters = {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "repetition_penalty": 1
        }
        self.model = Model(
            model_id=self.model_id,
            params=self.parameters,
            credentials=self.credentials,
            project_id=self.project_id
        )

    def generate_grammar_analysis(self, input_sentence):
        # Define the prompt to instruct the model
        prompt = (
            "<s> [INST] أنت مساعد لغوي تقوم بإعراب الجمل كما في المثال الموضح "
            f"المثال: "
            f"الجملة: قالت هند للمعلمة لماذا ذهبتي إلى القاعة "
            f"المخرج: {{ "
            f'"قالت": "فعل ماضٍ مبني على الفتح، والتاء للتأنيث", '
            f'"هند": "فاعل مرفوع وعلامة رفعه الضمة الظاهرة على آخره", '
            f'"للمعلمة": "اللام حرف جر، والمعلمة اسم مجرور وعلامة جره الكسرة الظاهرة على آخره، والجار والمجرور متعلقان بالفعل \'قالت\'", '
            f'"لماذا": "أداة استفهام مبنية على السكون في محل نصب مفعول به للفعل \'ذهبت\' لبيان سبب الذهاب", '
            f'"ذهبتِ": "فعل ماضٍ مبني على السكون، والتاء ضمير متصل مبني على الكسر في محل رفع فاعل", '
            f'"إلى": "حرف جر", '
            f'"القاعة": "اسم مجرور بـ \'إلى\' وعلامة جره الكسرة الظاهرة على آخره، والجار والمجرور متعلقان بالفعل \'ذهبت\'" '
            f"}} "
            "قم بإعراب الجملة المدخلة إليك إعرابا صحيحا كما في المثال "
            f"{input_sentence}"
        )
        output = self.model.generate_text(prompt)
        return output