











































"""
scene_generator.py — builds dream-like 3D scenes from text prompts.
"""

from typing import List, Dict
from engine.dream_graph import DreamGraph
from engine.texture_synth import TextureSynth


class SceneGenerator:
    def __init__(self):
        self.graph = DreamGraph()
        self.texture_synth = TextureSynth()

    def generate_scene(self, prompt: str) -> Dict:
        """
        Create a high-level 3D scene representation from a text prompt.
        """
        print(f"[DreamNet] Generating scene for prompt: {prompt}")
        nodes = self.graph.build_graph(prompt)
        textures = self.texture_synth.generate_textures(nodes)

        scene = {
            "prompt": prompt,
            "objects": nodes,
            "textures": textures,
            "lighting": self._generate_lighting(prompt),
            "atmosphere": self._generate_atmosphere(prompt),
        }

        print(f"[DreamNet] Scene generated with {len(nodes)} objects.")
        return scene

    def _generate_lighting(self, prompt: str) -> Dict:
        """
        Simple heuristic for lighting — changes tone depending on emotional weight of prompt.
        """
        mood_map = {
            "night": {"intensity": 0.2, "color": "blue"},
            "sunrise": {"intensity": 0.6, "color": "orange"},
            "dream": {"intensity": 0.4, "color": "lavender"},
        }
        for key, val in mood_map.items():
            if key in prompt.lower():
                return val
        return {"intensity": 0.5, "color": "neutral white"}

    def _generate_atmosphere(self, prompt: str) -> Dict:
        """
        Adds global volumetric atmosphere — fog, particles, etc.
        """
        if "water" in prompt.lower():
            return {"fog_density": 0.3, "ambient": "aqua"}
        elif "desert" in prompt.lower():
            return {"fog_density": 0.1, "ambient": "warm"}
        return {"fog_density": 0.2, "ambient": "soft"}


