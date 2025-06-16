import os
import unittest
from hash import calculer_hash_fichier, lister_fichiers_et_hashs, afficher_fichiers_duplicats

class TestHashChecker(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and files for testing."""
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        self.file1_path = os.path.join(self.test_dir, 'file1.txt')
        self.file2_path = os.path.join(self.test_dir, 'file2.txt')
        self.file3_path = os.path.join(self.test_dir, 'file3.txt')

        with open(self.file1_path, 'w') as f:
            f.write('Hello, World!')

        with open(self.file2_path, 'w') as f:
            f.write('Hello, World!')

        with open(self.file3_path, 'w') as f:
            f.write('Goodbye, World!')

    def tearDown(self):
        """Remove the temporary directory and files after testing."""
        for file in [self.file1_path, self.file2_path, self.file3_path]:
            if os.path.exists(file):
                os.remove(file)
        os.rmdir(self.test_dir)

    def test_calculer_hash_fichier(self):
        """Test the hash calculation for a file."""
        hash1 = calculer_hash_fichier(self.file1_path)
        hash2 = calculer_hash_fichier(self.file2_path)
        hash3 = calculer_hash_fichier(self.file3_path)

        self.assertEqual(hash1, hash2)
        self.assertNotEqual(hash1, hash3)

    def test_lister_fichiers_et_hashs(self):
        """Test listing files and their hashes."""
        fichiers_hashs = lister_fichiers_et_hashs(self.test_dir)
        self.assertIn(calculer_hash_fichier(self.file1_path), fichiers_hashs)
        self.assertIn(calculer_hash_fichier(self.file3_path), fichiers_hashs)
        self.assertEqual(len(fichiers_hashs), 2)  # file1 and file3 should have different hashes

    def test_afficher_fichiers_duplicats(self):
        """Test the display of duplicate files."""
        fichiers_hashs = lister_fichiers_et_hashs(self.test_dir)
        with self.assertLogs(level='INFO') as log:
            afficher_fichiers_duplicats(fichiers_hashs)
            self.assertIn('Hash:', log.output[0])  # Check if duplicates are logged

if __name__ == '__main__':
    unittest.main()