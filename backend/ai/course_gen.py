from .hf_config import HFConfig
import json
import re

class CourseGenerator:
    def __init__(self, model_name='mistral'):
        self.model_name = model_name
    
    def generate_course(self, language, level):
        if not HFConfig.validate_token():
            return self._get_fallback_course(language, level)
        
        try:
            client = HFConfig.get_client(self.model_name)
            prompt = self._build_course_prompt(language, level)
            
            response = client.text_generation(
                prompt,
                max_new_tokens=800,
                temperature=0.7,
                do_sample=True,
                return_full_text=False
            )
            
            return self._parse_course_response(response, language, level)
            
        except Exception as e:
            print(f"Erreur generation cours: {e}")
            return self._get_fallback_course(language, level)
    
    def _build_course_prompt(self, language, level):
        return f"""Genere un cours de programmation au format JSON.

Langage: {language}
Niveau: {level}

Retourne SEULEMENT du JSON valide"""

    def _parse_course_response(self, response, language, level):
        try:
            cleaned = re.sub(r'^[^{]*', '', response)
            cleaned = re.sub(r'[^}]*$', '', cleaned)
            return json.loads(cleaned)
        except:
            return self._get_fallback_course(language, level)
    
    def _get_fallback_course(self, language, level):
        return {
            "title": f"Introduction a {language.title()}",
            "language": language,
            "level": level,
            "sections": [
                {
                    "title": "Bases",
                    "content": f"Cours {language} pour {level} (mode secours)",
                    "code_examples": [f"# Exemple {language}"]
                }
            ],
            "learning_objectives": [f"Apprendre {language}"],
            "summary": f"Cours {language}"
        }
