import unittest
from pyiron_base import Project
from pyiron_base.archiving.export_archive import export_database
from pyiron_base.archiving import export_archive
from sample_job import ToyJob
import pandas as pd
from pandas._testing import assert_frame_equal

class TestPacking(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("set up the class")
        cls.pr = Project('test')
        cls.pr.remove_jobs_silently(recursive=True)
        cls.job = cls.pr.create_job(job_type=ToyJob, job_name="toy")
        cls.job.run()
        cls.pr.packing(destination_path='archive_folder',compress=false)
    
    def test_exportedCSV(self):
        ## in the first test, the csv file from the packing function is read
        ## and is compared with the return dataframe from export_database function   
        df_read = pd.read('export.csv')
        df_read.drop(df_read.keys()[0],inplace=True,axis = 1).dropna(inplace = True, axis=1) ## this remove the "None/NaN/empty" cells as well as the unnamed column
        df_read['timestart'] = pd.to_datetime(df_read['timestart'])
        df_read["hamversion"]= float(df_read["hamversion"])
        assert_frame_equal(export_database(self.pr, self.pr.path,'archive_folder').dropna(axis=1),df_read)
        ## In the second test, an examplary.csv file is read and compared with the
        ## one produced by the packing function
        df_known = pd.read_csv("exemplary.csv")
        df_read = pd.read('export.csv')
        df_known.dropna(inplace = True, axis= 1).drop(["timestart","computer"],inplace=True,axis=1)
        df_read.dropna(inplace = True, axis= 1).drop(["timestart","computer"],inplace=True,axis=1)
        assert_frame_equal(df_known,df_read) 
    
    def test_HDF5(self):
        pass

if __name__ == "__main__":
    unittest.main()