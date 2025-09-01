#!/usr/bin/env python3
"""
测试apted包的导入和基本功能
"""

def test_apted_import():
    """测试apted包的导入"""
    try:
        from apted import APTED, Config
        print("✓ apted包导入成功")
        
        # 测试基本功能
        class SimpleConfig(Config):
            def delete(self, node):
                return 1
            def insert(self, node):
                return 1
            def rename(self, node1, node2):
                return 0 if node1 == node2 else 1
        
        # 测试简单的树编辑距离计算
        tree1 = "a(b,c)"
        tree2 = "a(b,d)"
        
        config = SimpleConfig()
        apted = APTED(tree1, tree2, config)
        distance = apted.compute_edit_distance()
        
        print(f"✓ APTED基本功能测试成功，编辑距离: {distance}")
        return True
        
    except ImportError as e:
        print(f"✗ apted包导入失败: {e}")
        return False
    except Exception as e:
        print(f"✗ APTED功能测试失败: {e}")
        return False

if __name__ == "__main__":
    test_apted_import()
