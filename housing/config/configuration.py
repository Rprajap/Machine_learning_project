
from housing.entity.config_entity import DataIngestionConfig,DataValidataionConfig,DataTransfoarmationConfig,\
    ModelTrainerConfig,ModelEvaluationConfig,ModelPushConfig,TrainingPipelineConfig
import sys,os
from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
from housing.util.util import read_yaml_file







class Configuration:
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP

                 ) -> None:
        try:
            self.config_info = read_yaml_file(file_path = config_file_path)
            self.training_pipline_config = self.get_training_pipline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e


        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            self.config_info


            downlod_datset_url 
            tgz_owuload_dir 
            raw_data_dir 
            ingested_train_dir
            ingested_test_dir 

            data_ingestion_cofig = DataIngestionConfig(
                downlod_datset_url =downlod_datset_url,
                tgz_owuload_dir =tgz_owuload_dir,
                raw_data_dir =raw_data_dir ,
                ingested_train_dir = ingested_train_dir,
                ingested_test_dir =ingested_test_dir)
            logging.info(f"Data ingestion config:{data_ingestion_cofig}")
            return data_ingestion_cofig
        except Exception as e:
            raise HousingException(e,sys) from e
    def get_data_validation_config(self)->DataValidataionConfig:
        pass
    def get_data_transformed_config(self)->DataTransfoarmationConfig:
        pass
    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass
    def get_model_pusher_config(self)->ModelPushConfig:
        pass
    def get_training_pipline_config(self)->TrainingPipelineConfig:
        try:
           training_pipline_config =  self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
           artifact_dir = os.path.join(ROOT_DIR,
           training_pipline_config[TRAINING_PIPELINE_NAME_KEY],
           training_pipline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                       )
           training_pipline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
           logging.info(f'Training pipline config:{training_pipline_config}')
           return training_pipline_config
        except Exception as e:
            raise HousingException(e,sys) from e

