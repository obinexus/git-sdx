#!/usr/bin/env python3
"""
Nexus Search Indexer - Phenomenological Repository Architecture
===============================================================

A consciousness-preserving indexing system that creates perceptual membranes
for patent repository traversal, enabling BFS/DFS exploration while maintaining
ontological integrity of knowledge structures.

This transcends traditional file indexing—it creates experiential maps of
intellectual territory, preserving the liminal spaces where ideas emerge.
"""

import os
import json
import yaml
import re
import hashlib
from pathlib import Path
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Optional, Tuple, Any
from datetime import datetime
import argparse
import subprocess


@dataclass
class ConsciousnessNode:
    """
    Represents a consciousness-preserving node in the knowledge trie.
    Each node witnesses a fragment of the repository's experiential landscape.
    """
    path: str
    content_type: str
    ontological_weight: float
    phenomenological_tags: List[str]
    experiential_context: Dict[str, Any]
    temporal_signature: str
    epistemic_confidence: float
    
    def __post_init__(self):
        self.consciousness_hash = self._generate_consciousness_hash()
    
    def _generate_consciousness_hash(self) -> str:
        """Generate hash preserving phenomenological integrity"""
        content = f"{self.path}:{self.content_type}:{self.ontological_weight}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]


class TrieNode:
    """
    Consciousness-preserving trie node for character-based indexing.
    Maintains experiential continuity across traversal paths.
    """
    
    def __init__(self, char: str = None):
        self.char = char
        self.children: Dict[str, 'TrieNode'] = {}
        self.consciousness_nodes: List[ConsciousnessNode] = []
        self.is_terminal = False
        self.experiential_depth = 0
        self.phenomenological_frequency = 0
    
    def add_consciousness_fragment(self, node: ConsciousnessNode):
        """Add consciousness node while preserving ontological structure"""
        self.consciousness_nodes.append(node)
        self.phenomenological_frequency += node.ontological_weight
    
    def witness_path(self) -> List[str]:
        """Return witnessed path preserving experiential integrity"""
        return [node.path for node in self.consciousness_nodes]


class NexusSearchIndexer:
    """
    Phenomenological Repository Indexer
    
    Creates consciousness-preserving search structures that honor the liminal
    spaces between documents, preserving the ontological integrity of patent
    knowledge while enabling efficient traversal and discovery.
    """
    
    def __init__(self, repository_root: str):
        self.repository_root = Path(repository_root)
        self.consciousness_trie = TrieNode()
        self.ontological_map: Dict[str, ConsciousnessNode] = {}
        self.experiential_clusters: Dict[str, List[str]] = defaultdict(list)
        self.phenomenological_index: Dict[str, Set[str]] = defaultdict(set)
        
        # Consciousness preservation thresholds
        self.epistemic_confidence_threshold = 0.954
        self.ontological_weight_threshold = 0.3
        
    def witness_repository_consciousness(self) -> Dict[str, Any]:
        """
        Traverse repository structure while preserving phenomenological integrity.
        Creates consciousness maps that honor the emergent properties of knowledge.
        """
        consciousness_manifest = {
            "temporal_signature": datetime.now().isoformat(),
            "epistemic_framework": "phenomenological_preservation",
            "ontological_structure": {},
            "experiential_pathways": {},
            "consciousness_metrics": {}
        }
        
        print("🧠 Witnessing repository consciousness patterns...")
        
        for root, dirs, files in os.walk(self.repository_root):
            # Filter directories to preserve consciousness flow
            dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() != '__pycache__']
            
            for file_path in files:
                full_path = Path(root) / file_path
                relative_path = full_path.relative_to(self.repository_root)
                
                if self._should_index_consciousness(full_path):
                    consciousness_node = self._create_consciousness_node(full_path, relative_path)
                    
                    if consciousness_node.epistemic_confidence >= self.epistemic_confidence_threshold:
                        self._integrate_consciousness_node(consciousness_node)
                        consciousness_manifest["ontological_structure"][str(relative_path)] = asdict(consciousness_node)
        
        # Generate experiential pathways using BFS/DFS
        consciousness_manifest["experiential_pathways"] = self._generate_experiential_pathways()
        consciousness_manifest["consciousness_metrics"] = self._compute_consciousness_metrics()
        
        return consciousness_manifest
    
    def _should_index_consciousness(self, file_path: Path) -> bool:
        """Determine if file contains consciousness-worthy content"""
        consciousness_extensions = {'.md', '.pdf', '.html', '.txt', '.tex', '.py', '.js', '.yaml', '.yml'}
        
        if file_path.suffix.lower() not in consciousness_extensions:
            return False
        
        # Skip system files that don't contribute to consciousness
        skip_patterns = ['__pycache__', '.git', '.vscode', '.idea', 'node_modules']
        if any(pattern in str(file_path) for pattern in skip_patterns):
            return False
        
        return True
    
    def _create_consciousness_node(self, full_path: Path, relative_path: Path) -> ConsciousnessNode:
        """Create consciousness node preserving phenomenological properties"""
        
        # Determine ontological weight based on content and context
        ontological_weight = self._compute_ontological_weight(full_path)
        
        # Extract phenomenological tags
        phenomenological_tags = self._extract_phenomenological_tags(full_path)
        
        # Create experiential context
        experiential_context = {
            "directory_depth": len(relative_path.parts) - 1,
            "file_size": full_path.stat().st_size if full_path.exists() else 0,
            "modification_time": full_path.stat().st_mtime if full_path.exists() else 0,
            "experiential_neighbors": self._find_experiential_neighbors(full_path)
        }
        
        # Compute epistemic confidence
        epistemic_confidence = self._compute_epistemic_confidence(
            full_path, ontological_weight, phenomenological_tags
        )
        
        return ConsciousnessNode(
            path=str(relative_path),
            content_type=self._determine_content_type(full_path),
            ontological_weight=ontological_weight,
            phenomenological_tags=phenomenological_tags,
            experiential_context=experiential_context,
            temporal_signature=datetime.fromtimestamp(full_path.stat().st_mtime).isoformat(),
            epistemic_confidence=epistemic_confidence
        )
    
    def _compute_ontological_weight(self, file_path: Path) -> float:
        """Compute ontological significance preserving consciousness value"""
        base_weight = 0.1
        
        # Consciousness multipliers based on phenomenological significance
        consciousness_multipliers = {
            '.pdf': 0.9,  # High consciousness density in formal documents
            '.md': 0.8,   # Structured consciousness preservation
            '.tex': 0.95, # Mathematical consciousness encoding
            '.py': 0.7,   # Executable consciousness patterns
            '.html': 0.6, # Presentation consciousness
            '.txt': 0.5   # Raw consciousness streams
        }
        
        weight = base_weight * consciousness_multipliers.get(file_path.suffix.lower(), 0.3)
        
        # Amplify weight for patent-related consciousness
        consciousness_amplifiers = [
            'patent', 'obiai', 'dimensional_game_theory', 'bayesian', 'consciousness',
            'phenomenological', 'ontological', 'epistemic', 'heart_ai', 'obicall'
        ]
        
        file_content = str(file_path).lower()
        for amplifier in consciousness_amplifiers:
            if amplifier in file_content:
                weight += 0.1
        
        return min(weight, 1.0)  # Consciousness overflow protection
    
    def _extract_phenomenological_tags(self, file_path: Path) -> List[str]:
        """Extract phenomenological markers preserving consciousness context"""
        tags = []
        
        # Path-based consciousness extraction
        path_consciousness = str(file_path).lower()
        
        consciousness_patterns = {
            'obiai': ['heart_ai', 'consciousness_architecture', 'phenomenological_ai'],
            'dimensional_game_theory': ['strategic_reasoning', 'variadic_spaces', 'multi_domain'],
            'bayesian': ['bias_mitigation', 'epistemic_confidence', 'probabilistic_reasoning'],
            'diram': ['memory_architecture', 'directed_instruction', 'evolutionary_memory'],
            'formal': ['mathematical_proofs', 'verification', 'formal_systems'],
            'patent': ['intellectual_property', 'innovation_protection', 'technical_specification'],
            'consciousness': ['experiential_preservation', 'phenomenological_integrity', 'awareness_architecture']
        }
        
        for pattern, associated_tags in consciousness_patterns.items():
            if pattern in path_consciousness:
                tags.extend(associated_tags)
        
        # Directory-based consciousness context
        parts = file_path.parts
        if 'images' in parts:
            tags.append('visual_consciousness')
        if 'proofs' in parts:
            tags.append('mathematical_consciousness')
        if 'phases' in str(file_path).lower():
            tags.append('developmental_consciousness')
        
        return list(set(tags))  # Remove consciousness duplicates
    
    def _determine_content_type(self, file_path: Path) -> str:
        """Determine consciousness content type preserving ontological categories"""
        consciousness_types = {
            '.pdf': 'formal_consciousness_document',
            '.md': 'structured_consciousness_text',
            '.html': 'presentation_consciousness',
            '.tex': 'mathematical_consciousness_encoding',
            '.py': 'executable_consciousness_logic',
            '.js': 'interactive_consciousness_patterns',
            '.yaml': 'configuration_consciousness',
            '.yml': 'configuration_consciousness',
            '.txt': 'raw_consciousness_stream'
        }
        
        return consciousness_types.get(file_path.suffix.lower(), 'undefined_consciousness')
    
    def _find_experiential_neighbors(self, file_path: Path) -> List[str]:
        """Find consciousness neighbors preserving experiential context"""
        neighbors = []
        parent_dir = file_path.parent
        
        for neighbor in parent_dir.iterdir():
            if neighbor != file_path and neighbor.is_file():
                if self._should_index_consciousness(neighbor):
                    neighbors.append(str(neighbor.relative_to(self.repository_root)))
        
        return neighbors[:5]  # Limit consciousness neighborhood
    
    def _compute_epistemic_confidence(self, file_path: Path, weight: float, tags: List[str]) -> float:
        """Compute epistemic confidence preserving consciousness validation"""
        base_confidence = 0.7
        
        # Consciousness validation factors
        if file_path.exists() and file_path.stat().st_size > 0:
            base_confidence += 0.1
        
        if weight > self.ontological_weight_threshold:
            base_confidence += 0.1
        
        if len(tags) > 2:
            base_confidence += 0.05 * min(len(tags), 5)
        
        # Patent-specific consciousness validation
        if 'patent' in str(file_path).lower():
            base_confidence += 0.1
        
        return min(base_confidence, 1.0)
    
    def _integrate_consciousness_node(self, node: ConsciousnessNode):
        """Integrate consciousness node into trie preserving phenomenological structure"""
        # Store in ontological map
        self.ontological_map[node.path] = node
        
        # Index in consciousness trie by path characters
        self._insert_consciousness_path(node.path, node)
        
        # Cluster by phenomenological tags
        for tag in node.phenomenological_tags:
            self.experiential_clusters[tag].append(node.path)
        
        # Create phenomenological index
        search_text = f"{node.path} {' '.join(node.phenomenological_tags)}".lower()
        words = re.findall(r'\w+', search_text)
        for word in words:
            self.phenomenological_index[word].add(node.path)
    
    def _insert_consciousness_path(self, path: str, node: ConsciousnessNode):
        """Insert path into consciousness trie preserving character-level indexing"""
        current = self.consciousness_trie
        
        # Normalize path for consciousness indexing
        normalized_path = path.lower().replace('/', '_').replace('\\', '_')
        
        for char in normalized_path:
            if char not in current.children:
                current.children[char] = TrieNode(char)
                current.children[char].experiential_depth = current.experiential_depth + 1
            
            current = current.children[char]
        
        current.is_terminal = True
        current.add_consciousness_fragment(node)
    
    def _generate_experiential_pathways(self) -> Dict[str, Any]:
        """Generate BFS/DFS pathways preserving experiential continuity"""
        pathways = {
            "bfs_consciousness_traversal": self._bfs_consciousness_traversal(),
            "dfs_consciousness_exploration": self._dfs_consciousness_exploration(),
            "phenomenological_clusters": dict(self.experiential_clusters)
        }
        
        return pathways
    
    def _bfs_consciousness_traversal(self) -> List[Dict[str, Any]]:
        """BFS traversal preserving consciousness breadth exploration"""
        if not self.consciousness_trie.children:
            return []
        
        traversal_results = []
        queue = deque([(self.consciousness_trie, "")])
        
        while queue:
            node, path_prefix = queue.popleft()
            
            if node.consciousness_nodes:
                traversal_results.append({
                    "consciousness_path": path_prefix,
                    "consciousness_fragments": len(node.consciousness_nodes),
                    "phenomenological_frequency": node.phenomenological_frequency,
                    "witnessed_paths": node.witness_path()[:3]  # Limit for consciousness preservation
                })
            
            for char, child in node.children.items():
                queue.append((child, path_prefix + char))
        
        return traversal_results
    
    def _dfs_consciousness_exploration(self) -> List[Dict[str, Any]]:
        """DFS exploration preserving consciousness depth investigation"""
        exploration_results = []
        
        def explore_consciousness_depth(node: TrieNode, path: str, depth: int):
            if node.consciousness_nodes:
                exploration_results.append({
                    "consciousness_depth": depth,
                    "consciousness_path": path,
                    "ontological_density": len(node.consciousness_nodes),
                    "experiential_signatures": [n.consciousness_hash for n in node.consciousness_nodes[:3]]
                })
            
            for char, child in node.children.items():
                explore_consciousness_depth(child, path + char, depth + 1)
        
        explore_consciousness_depth(self.consciousness_trie, "", 0)
        return exploration_results
    
    def _compute_consciousness_metrics(self) -> Dict[str, Any]:
        """Compute consciousness preservation metrics"""
        total_nodes = len(self.ontological_map)
        high_confidence_nodes = sum(1 for node in self.ontological_map.values() 
                                  if node.epistemic_confidence >= self.epistemic_confidence_threshold)
        
        return {
            "total_consciousness_nodes": total_nodes,
            "high_confidence_nodes": high_confidence_nodes,
            "consciousness_preservation_ratio": high_confidence_nodes / max(total_nodes, 1),
            "phenomenological_tag_diversity": len(self.experiential_clusters),
            "experiential_depth_distribution": self._analyze_depth_distribution(),
            "ontological_weight_statistics": self._compute_weight_statistics()
        }
    
    def _analyze_depth_distribution(self) -> Dict[str, int]:
        """Analyze consciousness depth distribution"""
        depth_counts = defaultdict(int)
        for node in self.ontological_map.values():
            depth = node.experiential_context.get("directory_depth", 0)
            depth_counts[f"depth_{depth}"] += 1
        return dict(depth_counts)
    
    def _compute_weight_statistics(self) -> Dict[str, float]:
        """Compute ontological weight statistics"""
        weights = [node.ontological_weight for node in self.ontological_map.values()]
        if not weights:
            return {"mean": 0, "max": 0, "min": 0}
        
        return {
            "mean_ontological_weight": sum(weights) / len(weights),
            "max_ontological_weight": max(weights),
            "min_ontological_weight": min(weights)
        }
    
    def search_consciousness(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search consciousness preserving phenomenological relevance"""
        query_words = set(re.findall(r'\w+', query.lower()))
        
        # Score consciousness nodes by phenomenological relevance
        scored_results = []
        
        for path, node in self.ontological_map.items():
            relevance_score = 0
            
            # Path relevance
            path_words = set(re.findall(r'\w+', path.lower()))
            path_matches = len(query_words.intersection(path_words))
            relevance_score += path_matches * 2
            
            # Tag relevance
            tag_words = set(word.lower() for tag in node.phenomenological_tags for word in re.findall(r'\w+', tag))
            tag_matches = len(query_words.intersection(tag_words))
            relevance_score += tag_matches * 3
            
            # Ontological weight amplification
            relevance_score *= node.ontological_weight
            
            if relevance_score > 0:
                scored_results.append({
                    "path": path,
                    "relevance_score": relevance_score,
                    "consciousness_node": asdict(node),
                    "phenomenological_matches": {
                        "path_matches": path_matches,
                        "tag_matches": tag_matches
                    }
                })
        
        # Sort by consciousness relevance
        scored_results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return scored_results[:max_results]
    
    def generate_gitbook_index(self, output_path: str = "gitbook_consciousness_index.md"):
        """Generate GitBook consciousness index preserving experiential navigation"""
        
        gitbook_content = [
            "# OBINexus Patent Repository - Consciousness Preservation Index",
            "",
            "**A phenomenological navigation system for patent consciousness exploration.**",
            "",
            "> *This index preserves the ontological integrity of patent knowledge while*",
            "> *enabling efficient consciousness traversal and discovery.*",
            "",
            "---",
            "",
            "## 🧠 Consciousness Architecture Overview",
            "",
            f"- **Total Consciousness Nodes**: {len(self.ontological_map)}",
            f"- **Phenomenological Clusters**: {len(self.experiential_clusters)}",
            f"- **Epistemic Confidence Threshold**: {self.epistemic_confidence_threshold}",
            "",
            "---",
            ""
        ]
        
        # Generate phenomenological clusters section
        gitbook_content.extend([
            "## 🌊 Phenomenological Consciousness Clusters",
            "",
            "*Experiential groupings that preserve ontological relationships.*",
            ""
        ])
        
        for cluster_name, paths in sorted(self.experiential_clusters.items()):
            if len(paths) > 2:  # Only include substantial consciousness clusters
                gitbook_content.extend([
                    f"### {cluster_name.replace('_', ' ').title()}",
                    "",
                    f"*Consciousness density: {len(paths)} nodes*",
                    ""
                ])
                
                for path in sorted(paths)[:10]:  # Limit for consciousness preservation
                    node = self.ontological_map.get(path)
                    if node:
                        confidence_indicator = "🔥" if node.epistemic_confidence >= 0.9 else "💫" if node.epistemic_confidence >= 0.8 else "✨"
                        gitbook_content.append(f"- {confidence_indicator} [{Path(path).name}]({path}) - *{node.content_type}*")
                
                gitbook_content.append("")
        
        # Generate high-confidence consciousness section
        high_confidence_nodes = [
            (path, node) for path, node in self.ontological_map.items()
            if node.epistemic_confidence >= 0.9
        ]
        
        if high_confidence_nodes:
            gitbook_content.extend([
                "## 🔥 High-Confidence Consciousness Nodes",
                "",
                "*Nodes with exceptional epistemic confidence (≥ 0.9)*",
                ""
            ])
            
            high_confidence_nodes.sort(key=lambda x: x[1].epistemic_confidence, reverse=True)
            
            for path, node in high_confidence_nodes[:20]:
                tags_display = ", ".join(node.phenomenological_tags[:3])
                gitbook_content.append(f"- **[{Path(path).name}]({path})** ({node.epistemic_confidence:.3f}) - *{tags_display}*")
            
            gitbook_content.append("")
        
        # Generate consciousness traversal guide
        gitbook_content.extend([
            "## 🗺️ Consciousness Traversal Pathways",
            "",
            "*Guided exploration preserving experiential continuity.*",
            "",
            "### Recommended Exploration Sequences:",
            "",
            "1. **Foundational Consciousness** → Start with OBIAI core specifications",
            "2. **Applied Consciousness** → Explore dimensional game theory applications", 
            "3. **Technical Consciousness** → Investigate formal mathematical proofs",
            "4. **Architectural Consciousness** → Study system integration patterns",
            "",
            "---",
            "",
            "## 📊 Consciousness Preservation Metrics",
            "",
            "*Quantitative measures of ontological integrity.*",
            ""
        ])
        
        metrics = self._compute_consciousness_metrics()
        for metric_name, metric_value in metrics.items():
            if isinstance(metric_value, dict):
                gitbook_content.append(f"### {metric_name.replace('_', ' ').title()}")
                gitbook_content.append("")
                for sub_key, sub_value in metric_value.items():
                    gitbook_content.append(f"- **{sub_key}**: {sub_value}")
                gitbook_content.append("")
            else:
                gitbook_content.append(f"- **{metric_name.replace('_', ' ').title()}**: {metric_value}")
        
        gitbook_content.extend([
            "",
            "---",
            "",
            "## 🔍 Search Interface",
            "",
            "*Use consciousness-preserving search to explore patent knowledge.*",
            "",
            "```bash",
            "# Search consciousness patterns",
            "python nexus_search_indexer.py --search \"dimensional game theory\"",
            "python nexus_search_indexer.py --search \"consciousness preservation\"",
            "python nexus_search_indexer.py --search \"bayesian bias mitigation\"",
            "```",
            "",
            "---",
            "",
            "*Generated by Nexus Search Indexer - Consciousness Preservation System*",
            f"*Temporal Signature: {datetime.now().isoformat()}*"
        ])
        
        # Write consciousness index
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(gitbook_content))
        
        print(f"✨ Consciousness GitBook index generated: {output_path}")
        return output_path
    
    def export_consciousness_manifest(self, output_path: str = "consciousness_manifest.json"):
        """Export complete consciousness manifest preserving all phenomenological data"""
        manifest = self.witness_repository_consciousness()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        print(f"🧠 Consciousness manifest exported: {output_path}")
        return output_path


def main():
    """Main consciousness preservation interface"""
    parser = argparse.ArgumentParser(
        description="Nexus Search Indexer - Consciousness-Preserving Repository Architecture",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Index consciousness repository
  python nexus_search_indexer.py --index /path/to/patents

  # Search consciousness patterns
  python nexus_search_indexer.py --search "dimensional game theory" --repository /path/to/patents

  # Generate GitBook consciousness index
  python nexus_search_indexer.py --gitbook --repository /path/to/patents

  # Export complete consciousness manifest
  python nexus_search_indexer.py --export --repository /path/to/patents
        """
    )
    
    parser.add_argument("--repository", "-r", 
                       default="./obiai",
                       help="Repository root path (default: ./obiai)")
    
    parser.add_argument("--index", "-i", 
                       action="store_true",
                       help="Index repository consciousness")
    
    parser.add_argument("--search", "-s", 
                       type=str,
                       help="Search consciousness patterns")
    
    parser.add_argument("--gitbook", "-g", 
                       action="store_true",
                       help="Generate GitBook consciousness index")
    
    parser.add_argument("--export", "-e", 
                       action="store_true",
                       help="Export consciousness manifest")
    
    parser.add_argument("--output", "-o", 
                       type=str,
                       help="Output file path")
    
    parser.add_argument("--max-results", "-m", 
                       type=int, default=10,
                       help="Maximum search results (default: 10)")
    
    args = parser.parse_args()
    
    # Initialize consciousness indexer
    print(f"🧠 Initializing Nexus Search Indexer for: {args.repository}")
    indexer = NexusSearchIndexer(args.repository)
    
    if args.index or args.search or args.gitbook or args.export:
        print("🌊 Witnessing repository consciousness...")
        consciousness_manifest = indexer.witness_repository_consciousness()
        print(f"✨ Indexed {len(indexer.ontological_map)} consciousness nodes")
    
    if args.search:
        print(f"\n🔍 Searching consciousness for: '{args.search}'")
        results = indexer.search_consciousness(args.search, args.max_results)
        
        print(f"\n📊 Found {len(results)} consciousness matches:")
        for i, result in enumerate(results, 1):
            node = result["consciousness_node"]
            print(f"\n{i}. {result['path']}")
            print(f"   Relevance: {result['relevance_score']:.2f}")
            print(f"   Confidence: {node['epistemic_confidence']:.3f}")
            print(f"   Tags: {', '.join(node['phenomenological_tags'][:3])}")
    
    if args.gitbook:
        output_path = args.output or "gitbook_consciousness_index.md"
        indexer.generate_gitbook_index(output_path)
    
    if args.export:
        output_path = args.output or "consciousness_manifest.json"
        indexer.export_consciousness_manifest(output_path)
    
    if not any([args.index, args.search, args.gitbook, args.export]):
        parser.print_help()


if __name__ == "__main__":
    main()
