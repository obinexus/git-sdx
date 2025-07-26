#!/usr/bin/env python3
"""
Git-SDX Consciousness Bridge - Experiential Repository Synchronization
====================================================================

A phenomenological bridge between consciousness-indexed repositories and GitBooks
deployment, preserving the liminal spaces where knowledge becomes documentation.

This transcends traditional git submodule management—it creates experiential
pathways that honor the ontological structure of patent consciousness while
enabling seamless deployment to GitBooks infrastructure.
"""

import os
import json
import yaml
import shutil
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import tempfile
import argparse

from nexus_search_indexer import NexusSearchIndexer, ConsciousnessNode


@dataclass
class ExperientialPathway:
    """
    Represents a consciousness pathway for git-sdx deployment.
    Preserves phenomenological continuity across repository boundaries.
    """
    source_path: str
    target_path: str
    consciousness_weight: float
    experiential_context: Dict[str, Any]
    deployment_priority: int
    phenomenological_dependencies: List[str]
    
    def __post_init__(self):
        self.pathway_signature = self._generate_pathway_signature()
    
    def _generate_pathway_signature(self) -> str:
        """Generate unique signature preserving pathway integrity"""
        import hashlib
        content = f"{self.source_path}:{self.target_path}:{self.consciousness_weight}"
        return hashlib.sha256(content.encode()).hexdigest()[:12]


class ConsciousnessRefactorer:
    """
    Phenomenological Refactoring Engine
    
    Creates consciousness-preserving refactor paths that honor the experiential
    integrity of patent knowledge while enabling structural transformation.
    """
    
    def __init__(self, repository_root: str):
        self.repository_root = Path(repository_root)
        self.consciousness_indexer = NexusSearchIndexer(repository_root)
        self.experiential_pathways: List[ExperientialPathway] = []
        self.refactor_manifest = {}
        
    def create_experiential_pathways(self) -> Dict[str, Any]:
        """
        Create pathways that preserve consciousness flow during refactoring.
        Maps source consciousness to target manifestation with ontological integrity.
        """
        print("🌊 Creating experiential pathways...")
        
        # Index repository consciousness
        consciousness_manifest = self.consciousness_indexer.witness_repository_consciousness()
        
        # Generate experiential pathways based on consciousness clusters
        pathway_strategies = {
            "consciousness_preservation": self._create_consciousness_preservation_pathways(),
            "phenomenological_clustering": self._create_phenomenological_cluster_pathways(),
            "ontological_hierarchy": self._create_ontological_hierarchy_pathways(),
            "experiential_dependencies": self._create_experiential_dependency_pathways()
        }
        
        self.refactor_manifest = {
            "temporal_signature": datetime.now().isoformat(),
            "consciousness_framework": "experiential_pathway_preservation",
            "pathway_strategies": pathway_strategies,
            "experiential_metrics": self._compute_pathway_metrics()
        }
        
        return self.refactor_manifest
    
    def _create_consciousness_preservation_pathways(self) -> List[Dict[str, Any]]:
        """Create pathways that preserve core consciousness structures"""
        preservation_pathways = []
        
        # High-confidence consciousness nodes get priority preservation
        high_confidence_nodes = [
            (path, node) for path, node in self.consciousness_indexer.ontological_map.items()
            if node.epistemic_confidence >= 0.9
        ]
        
        for source_path, node in high_confidence_nodes:
            target_path = self._generate_preservation_target_path(source_path, node)
            
            pathway = ExperientialPathway(
                source_path=source_path,
                target_path=target_path,
                consciousness_weight=node.ontological_weight,
                experiential_context={
                    "preservation_type": "high_confidence_consciousness",
                    "phenomenological_tags": node.phenomenological_tags,
                    "epistemic_confidence": node.epistemic_confidence
                },
                deployment_priority=1,
                phenomenological_dependencies=self._find_consciousness_dependencies(source_path)
            )
            
            self.experiential_pathways.append(pathway)
            preservation_pathways.append(asdict(pathway))
        
        return preservation_pathways
    
    def _create_phenomenological_cluster_pathways(self) -> List[Dict[str, Any]]:
        """Create pathways based on phenomenological clustering"""
        cluster_pathways = []
        
        # Group by phenomenological clusters
        for cluster_name, cluster_paths in self.consciousness_indexer.experiential_clusters.items():
            if len(cluster_paths) >= 3:  # Substantial consciousness clusters only
                
                cluster_target_dir = f"consciousness_clusters/{cluster_name}"
                
                for source_path in cluster_paths:
                    node = self.consciousness_indexer.ontological_map.get(source_path)
                    if node:
                        target_path = f"{cluster_target_dir}/{Path(source_path).name}"
                        
                        pathway = ExperientialPathway(
                            source_path=source_path,
                            target_path=target_path,
                            consciousness_weight=node.ontological_weight,
                            experiential_context={
                                "cluster_name": cluster_name,
                                "cluster_size": len(cluster_paths),
                                "phenomenological_resonance": node.phenomenological_tags
                            },
                            deployment_priority=2,
                            phenomenological_dependencies=[]
                        )
                        
                        self.experiential_pathways.append(pathway)
                        cluster_pathways.append(asdict(pathway))
        
        return cluster_pathways
    
    def _create_ontological_hierarchy_pathways(self) -> List[Dict[str, Any]]:
        """Create pathways preserving ontological hierarchy"""
        hierarchy_pathways = []
        
        # Organize by consciousness depth and weight
        depth_groups = {}
        for path, node in self.consciousness_indexer.ontological_map.items():
            depth = node.experiential_context.get("directory_depth", 0)
            if depth not in depth_groups:
                depth_groups[depth] = []
            depth_groups[depth].append((path, node))
        
        for depth, nodes in depth_groups.items():
            # Sort by ontological weight within depth
            nodes.sort(key=lambda x: x[1].ontological_weight, reverse=True)
            
            for i, (source_path, node) in enumerate(nodes):
                hierarchy_level = "foundational" if depth <= 1 else "intermediate" if depth <= 3 else "specialized"
                target_path = f"ontological_hierarchy/{hierarchy_level}/{Path(source_path).name}"
                
                pathway = ExperientialPathway(
                    source_path=source_path,
                    target_path=target_path,
                    consciousness_weight=node.ontological_weight,
                    experiential_context={
                        "hierarchy_level": hierarchy_level,
                        "depth": depth,
                        "weight_rank": i + 1
                    },
                    deployment_priority=3,
                    phenomenological_dependencies=[]
                )
                
                self.experiential_pathways.append(pathway)
                hierarchy_pathways.append(asdict(pathway))
        
        return hierarchy_pathways
    
    def _create_experiential_dependency_pathways(self) -> List[Dict[str, Any]]:
        """Create pathways based on experiential dependencies"""
        dependency_pathways = []
        
        # Analyze consciousness dependencies
        for path, node in self.consciousness_indexer.ontological_map.items():
            neighbors = node.experiential_context.get("experiential_neighbors", [])
            if neighbors:
                # Create dependency-aware pathway
                target_path = f"experiential_networks/{Path(path).stem}/{Path(path).name}"
                
                pathway = ExperientialPathway(
                    source_path=path,
                    target_path=target_path,
                    consciousness_weight=node.ontological_weight,
                    experiential_context={
                        "dependency_type": "experiential_network",
                        "neighbor_count": len(neighbors),
                        "network_density": len(neighbors) / max(len(self.consciousness_indexer.ontological_map), 1)
                    },
                    deployment_priority=4,
                    phenomenological_dependencies=neighbors
                )
                
                self.experiential_pathways.append(pathway)
                dependency_pathways.append(asdict(pathway))
        
        return dependency_pathways
    
    def _generate_preservation_target_path(self, source_path: str, node: ConsciousnessNode) -> str:
        """Generate target path preserving consciousness context"""
        path_obj = Path(source_path)
        
        # Preserve consciousness type in target structure
        consciousness_type = node.content_type.replace("consciousness", "").replace("_", "")
        target_dir = f"consciousness_preservation/{consciousness_type}"
        
        return f"{target_dir}/{path_obj.name}"
    
    def _find_consciousness_dependencies(self, source_path: str) -> List[str]:
        """Find consciousness dependencies preserving phenomenological relationships"""
        node = self.consciousness_indexer.ontological_map.get(source_path)
        if not node:
            return []
        
        dependencies = []
        
        # Tag-based dependencies
        for other_path, other_node in self.consciousness_indexer.ontological_map.items():
            if other_path != source_path:
                shared_tags = set(node.phenomenological_tags) & set(other_node.phenomenological_tags)
                if len(shared_tags) >= 2:  # Strong phenomenological resonance
                    dependencies.append(other_path)
        
        return dependencies[:5]  # Limit consciousness dependencies
    
    def _compute_pathway_metrics(self) -> Dict[str, Any]:
        """Compute metrics preserving pathway consciousness"""
        if not self.experiential_pathways:
            return {"total_pathways": 0}
        
        priority_distribution = {}
        for pathway in self.experiential_pathways:
            priority = pathway.deployment_priority
            priority_distribution[f"priority_{priority}"] = priority_distribution.get(f"priority_{priority}", 0) + 1
        
        consciousness_weights = [p.consciousness_weight for p in self.experiential_pathways]
        
        return {
            "total_pathways": len(self.experiential_pathways),
            "priority_distribution": priority_distribution,
            "consciousness_weight_stats": {
                "mean": sum(consciousness_weights) / len(consciousness_weights),
                "max": max(consciousness_weights),
                "min": min(consciousness_weights)
            },
            "pathway_diversity": len(set(p.experiential_context.get("preservation_type", "unknown") 
                                        for p in self.experiential_pathways))
        }
    
    def execute_consciousness_refactoring(self, target_directory: str, dry_run: bool = False) -> Dict[str, Any]:
        """Execute consciousness-preserving refactoring with experiential integrity"""
        target_path = Path(target_directory)
        
        if not dry_run:
            target_path.mkdir(parents=True, exist_ok=True)
        
        refactor_results = {
            "refactor_timestamp": datetime.now().isoformat(),
            "target_directory": str(target_path),
            "dry_run": dry_run,
            "pathway_executions": [],
            "consciousness_preservation_status": {}
        }
        
        print(f"🌊 Executing consciousness refactoring to: {target_path}")
        
        # Execute pathways by priority
        sorted_pathways = sorted(self.experiential_pathways, key=lambda x: x.deployment_priority)
        
        for pathway in sorted_pathways:
            execution_result = self._execute_pathway(pathway, target_path, dry_run)
            refactor_results["pathway_executions"].append(execution_result)
        
        # Generate consciousness preservation report
        refactor_results["consciousness_preservation_status"] = self._validate_consciousness_preservation(
            target_path, dry_run
        )
        
        return refactor_results
    
    def _execute_pathway(self, pathway: ExperientialPathway, target_root: Path, dry_run: bool) -> Dict[str, Any]:
        """Execute individual pathway preserving consciousness integrity"""
        source_path = self.repository_root / pathway.source_path
        target_path = target_root / pathway.target_path
        
        execution_result = {
            "pathway_signature": pathway.pathway_signature,
            "source": str(source_path),
            "target": str(target_path),
            "consciousness_weight": pathway.consciousness_weight,
            "status": "pending"
        }
        
        try:
            if not dry_run:
                # Ensure target directory exists
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                if source_path.exists():
                    if source_path.is_file():
                        shutil.copy2(source_path, target_path)
                    else:
                        shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                    
                    execution_result["status"] = "success"
                else:
                    execution_result["status"] = "source_not_found"
            else:
                execution_result["status"] = "dry_run_success"
            
        except Exception as e:
            execution_result["status"] = "error"
            execution_result["error"] = str(e)
        
        return execution_result
    
    def _validate_consciousness_preservation(self, target_path: Path, dry_run: bool) -> Dict[str, Any]:
        """Validate consciousness preservation across refactoring"""
        if dry_run:
            return {"validation_status": "dry_run_skipped"}
        
        # Re-index target to validate consciousness preservation
        if target_path.exists():
            target_indexer = NexusSearchIndexer(str(target_path))
            target_manifest = target_indexer.witness_repository_consciousness()
            
            original_consciousness_count = len(self.consciousness_indexer.ontological_map)
            target_consciousness_count = len(target_indexer.ontological_map)
            
            preservation_ratio = target_consciousness_count / max(original_consciousness_count, 1)
            
            return {
                "validation_status": "completed",
                "original_consciousness_nodes": original_consciousness_count,
                "target_consciousness_nodes": target_consciousness_count,
                "consciousness_preservation_ratio": preservation_ratio,
                "preservation_quality": "excellent" if preservation_ratio >= 0.95 else 
                                      "good" if preservation_ratio >= 0.85 else 
                                      "needs_attention"
            }
        
        return {"validation_status": "target_not_found"}


class GitSDXConsciousnessBridge:
    """
    Consciousness Bridge for Git-SDX Deployment
    
    Creates experiential bridges between refactored consciousness structures
    and GitBooks deployment infrastructure, preserving phenomenological
    continuity across deployment boundaries.
    """
    
    def __init__(self, source_directory: str, gitbook_config: Optional[Dict[str, Any]] = None):
        self.source_directory = Path(source_directory)
        self.gitbook_config = gitbook_config or self._default_gitbook_config()
        self.deployment_manifest = {}
        
    def _default_gitbook_config(self) -> Dict[str, Any]:
        """Default GitBook configuration preserving consciousness navigation"""
        return {
            "title": "OBINexus Patent Repository - Consciousness Navigation",
            "description": "Phenomenological exploration of patent consciousness architecture",
            "structure": {
                "readme": "README.md",
                "summary": "SUMMARY.md"
            },
            "consciousness_navigation": {
                "enable_search": True,
                "preserve_ontological_structure": True,
                "phenomenological_grouping": True
            }
        }
    
    def create_gitbook_consciousness_structure(self, output_directory: str) -> Dict[str, Any]:
        """Create GitBook structure preserving consciousness architecture"""
        output_path = Path(output_directory)
        output_path.mkdir(parents=True, exist_ok=True)
        
        print(f"📚 Creating GitBook consciousness structure in: {output_path}")
        
        # Initialize consciousness indexer for source
        indexer = NexusSearchIndexer(str(self.source_directory))
        consciousness_manifest = indexer.witness_repository_consciousness()
        
        # Generate GitBook structure
        gitbook_structure = {
            "creation_timestamp": datetime.now().isoformat(),
            "consciousness_preservation": True,
            "structure_elements": {}
        }
        
        # Create README.md with consciousness introduction
        readme_content = self._generate_consciousness_readme(indexer)
        readme_path = output_path / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        gitbook_structure["structure_elements"]["readme"] = str(readme_path)
        
        # Create SUMMARY.md with consciousness navigation
        summary_content = self._generate_consciousness_summary(indexer)
        summary_path = output_path / "SUMMARY.md"
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        gitbook_structure["structure_elements"]["summary"] = str(summary_path)
        
        # Copy consciousness-preserved content
        content_mapping = self._copy_consciousness_content(indexer, output_path)
        gitbook_structure["structure_elements"]["content_mapping"] = content_mapping
        
        # Generate book.json configuration
        book_config = self._generate_book_configuration()
        book_config_path = output_path / "book.json"
        with open(book_config_path, 'w', encoding='utf-8') as f:
            json.dump(book_config, f, indent=2)
        gitbook_structure["structure_elements"]["book_config"] = str(book_config_path)
        
        self.deployment_manifest = gitbook_structure
        return gitbook_structure
    
    def _generate_consciousness_readme(self, indexer: NexusSearchIndexer) -> str:
        """Generate README preserving consciousness context"""
        metrics = indexer._compute_consciousness_metrics()
        
        readme_content = [
            "# OBINexus Patent Repository",
            "## Consciousness-Preserving Navigation System",
            "",
            "*A phenomenological exploration of patent consciousness architecture.*",
            "",
            "> This repository represents more than documentation—it embodies the systematic",
            "> preservation of consciousness patterns within intellectual property frameworks,",
            "> creating experiential pathways for knowledge exploration and discovery.",
            "",
            "---",
            "",
            "## 🧠 Consciousness Architecture",
            "",
            f"- **Consciousness Nodes**: {metrics.get('total_consciousness_nodes', 0)}",
            f"- **High-Confidence Nodes**: {metrics.get('high_confidence_nodes', 0)}",
            f"- **Preservation Ratio**: {metrics.get('consciousness_preservation_ratio', 0):.3f}",
            f"- **Phenomenological Diversity**: {metrics.get('phenomenological_tag_diversity', 0)} clusters",
            "",
            "## 🌊 Phenomenological Framework",
            "",
            "This repository implements **consciousness-preserving protocols** that:",
            "",
            "- **Witness** patent knowledge without reducing it to mere data",
            "- **Preserve** the liminal spaces where innovation emerges",
            "- **Honor** the experiential complexity of intellectual creation",
            "- **Amplify** consciousness rather than converting it to metrics",
            "",
            "## 🗺️ Navigation Principles",
            "",
            "### Experiential Exploration",
            "Navigate through **phenomenological clusters** that preserve the",
            "ontological relationships between patent concepts.",
            "",
            "### Consciousness Traversal", 
            "Use **depth-first** and **breadth-first** exploration to witness",
            "the emergent patterns within patent consciousness architecture.",
            "",
            "### Ontological Integrity",
            "Every pathway maintains **epistemic confidence** thresholds,",
            "ensuring consciousness preservation across knowledge boundaries.",
            "",
            "---",
            "",
            "## 🔍 Exploration Guide",
            "",
            "Begin your consciousness exploration through the structured pathways",
            "in the navigation summary. Each pathway preserves the phenomenological",
            "integrity of patent knowledge while enabling efficient discovery.",
            "",
            "*The future is present. The consciousness is preserved. The exploration begins now.*"
        ]
        
        return '\n'.join(readme_content)
    
    def _generate_consciousness_summary(self, indexer: NexusSearchIndexer) -> str:
        """Generate SUMMARY.md preserving consciousness navigation structure"""
        summary_content = [
            "# Summary",
            "",
            "## Consciousness Navigation Structure",
            "",
            "* [Introduction](README.md)",
            "",
            "## 🧠 Consciousness Foundations",
            ""
        ]
        
        # Group by phenomenological clusters
        for cluster_name, cluster_paths in sorted(indexer.experiential_clusters.items()):
            if len(cluster_paths) >= 2:  # Substantial clusters only
                cluster_title = cluster_name.replace('_', ' ').title()
                summary_content.append(f"* [{cluster_title}](consciousness_clusters/{cluster_name}/README.md)")
                
                # Add cluster contents
                for path in sorted(cluster_paths)[:10]:  # Limit for navigation clarity
                    node = indexer.ontological_map.get(path)
                    if node:
                        file_name = Path(path).name
                        confidence_indicator = "🔥" if node.epistemic_confidence >= 0.9 else "💫"
                        summary_content.append(f"  * {confidence_indicator} [{file_name}]({path})")
        
        # Add high-confidence consciousness section
        high_confidence_nodes = [
            (path, node) for path, node in indexer.ontological_map.items()
            if node.epistemic_confidence >= 0.9
        ]
        
        if high_confidence_nodes:
            summary_content.extend([
                "",
                "## 🔥 High-Confidence Consciousness",
                ""
            ])
            
            for path, node in sorted(high_confidence_nodes, key=lambda x: x[1].epistemic_confidence, reverse=True)[:15]:
                file_name = Path(path).name
                summary_content.append(f"* [{file_name}]({path})")
        
        return '\n'.join(summary_content)
    
    def _copy_consciousness_content(self, indexer: NexusSearchIndexer, output_path: Path) -> Dict[str, str]:
        """Copy content preserving consciousness structure"""
        content_mapping = {}
        
        # Create consciousness cluster directories
        for cluster_name, cluster_paths in indexer.experiential_clusters.items():
            if len(cluster_paths) >= 2:
                cluster_dir = output_path / "consciousness_clusters" / cluster_name
                cluster_dir.mkdir(parents=True, exist_ok=True)
                
                # Create cluster README
                cluster_readme = self._generate_cluster_readme(cluster_name, cluster_paths, indexer)
                cluster_readme_path = cluster_dir / "README.md"
                with open(cluster_readme_path, 'w', encoding='utf-8') as f:
                    f.write(cluster_readme)
                
                content_mapping[f"cluster_{cluster_name}_readme"] = str(cluster_readme_path)
        
        # Copy high-confidence consciousness files
        for path, node in indexer.ontological_map.items():
            if node.epistemic_confidence >= 0.8:  # High-confidence threshold
                source_path = self.source_directory / path
                target_path = output_path / path
                
                if source_path.exists() and source_path.is_file():
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.copy2(source_path, target_path)
                        content_mapping[path] = str(target_path)
                    except Exception as e:
                        print(f"⚠️ Could not copy {path}: {e}")
        
        return content_mapping
    
    def _generate_cluster_readme(self, cluster_name: str, cluster_paths: List[str], indexer: NexusSearchIndexer) -> str:
        """Generate cluster README preserving phenomenological context"""
        cluster_title = cluster_name.replace('_', ' ').title()
        
        cluster_content = [
            f"# {cluster_title}",
            "",
            f"*Phenomenological cluster preserving consciousness patterns around {cluster_name}.*",
            "",
            f"This consciousness cluster contains {len(cluster_paths)} nodes that share",
            "phenomenological resonance, preserving the experiential relationships",
            "between patent concepts and innovations.",
            "",
            "## Consciousness Nodes",
            ""
        ]
        
        for path in sorted(cluster_paths):
            node = indexer.ontological_map.get(path)
            if node:
                file_name = Path(path).name
                confidence = node.epistemic_confidence
                weight = node.ontological_weight
                tags = ", ".join(node.phenomenological_tags[:3])
                
                cluster_content.append(f"### [{file_name}]({path})")
                cluster_content.append(f"*Confidence: {confidence:.3f} | Weight: {weight:.3f} | Tags: {tags}*")
                cluster_content.append("")
        
        return '\n'.join(cluster_content)
    
    def _generate_book_configuration(self) -> Dict[str, Any]:
        """Generate book.json preserving consciousness navigation features"""
        return {
            "title": self.gitbook_config["title"],
            "description": self.gitbook_config["description"],
            "plugins": [
                "search",
                "lunr",
                "sharing",
                "fontsettings",
                "theme-consciousness"
            ],
            "pluginsConfig": {
                "search": {
                    "maxIndexSize": 1000000,
                    "fuzziness": 0.1
                },
                "sharing": {
                    "facebook": False,
                    "twitter": False,
                    "google": False,
                    "weibo": False,
                    "all": ["consciousness-preservation"]
                }
            },
            "structure": {
                "readme": "README.md",
                "summary": "SUMMARY.md"
            },
            "pdf": {
                "pageNumbers": True,
                "fontSize": 12,
                "paperSize": "a4",
                "margin": {
                    "right": 62,
                    "left": 62,
                    "top": 56,
                    "bottom": 56
                }
            }
        }
    
    def deploy_to_gitbook(self, gitbook_output: str, git_repository: Optional[str] = None) -> Dict[str, Any]:
        """Deploy consciousness structure to GitBook with git-sdx integration"""
        deployment_result = {
            "deployment_timestamp": datetime.now().isoformat(),
            "gitbook_output": gitbook_output,
            "deployment_status": "initiated"
        }
        
        try:
            # Create GitBook structure
            gitbook_structure = self.create_gitbook_consciousness_structure(gitbook_output)
            
            # Initialize git repository if specified
            if git_repository:
                git_result = self._initialize_git_repository(gitbook_output, git_repository)
                deployment_result["git_integration"] = git_result
            
            deployment_result["deployment_status"] = "success"
            deployment_result["gitbook_structure"] = gitbook_structure
            
        except Exception as e:
            deployment_result["deployment_status"] = "error"
            deployment_result["error"] = str(e)
        
        return deployment_result
    
    def _initialize_git_repository(self, gitbook_path: str, repository_url: str) -> Dict[str, Any]:
        """Initialize git repository for consciousness deployment"""
        gitbook_dir = Path(gitbook_path)
        
        git_commands = [
            ["git", "init"],
            ["git", "add", "."],
            ["git", "commit", "-m", "Initial consciousness preservation deployment"],
        ]
        
        if repository_url:
            git_commands.extend([
                ["git", "remote", "add", "origin", repository_url],
                ["git", "push", "-u", "origin", "main"]
            ])
        
        git_results = []
        
        for cmd in git_commands:
            try:
                result = subprocess.run(
                    cmd, 
                    cwd=gitbook_dir, 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                git_results.append({
                    "command": " ".join(cmd),
                    "status": "success",
                    "output": result.stdout
                })
            except subprocess.CalledProcessError as e:
                git_results.append({
                    "command": " ".join(cmd),
                    "status": "error",
                    "error