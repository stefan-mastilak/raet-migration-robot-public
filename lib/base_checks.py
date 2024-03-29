# REF: stefan.mastilak@visma.com

from lib.base_migration import Migration
import config as cfg
import logging
import os


class Checks(Migration):
    """
    Base checks class containing common methods for all migration types.
    """
    @staticmethod
    def pentaho_check():
        """
        Check if Pentaho installation path exists on the server.
        :return: True if Pentaho installation path exists
        :rtype: bool
        """
        if os.path.exists(cfg.PENTAHO_DIR):
            return True
        else:
            logging.fatal(msg=f" Pentaho path doesn't exist in {cfg.PENTAHO_DIR}")
            return False

    @staticmethod
    def kitchen_check():
        """
        Check if Kitchen.bat script exists in Pentaho installation directory.
        :return: True if Kitchen.bat script path exists
        :rtype: bool
        """
        kitchen_path = os.path.join(cfg.PENTAHO_DIR, 'Kitchen.bat')
        if os.path.isfile(kitchen_path):
            return True
        else:
            logging.critical(msg=f' Kitchen.bat script doesnt exist in {kitchen_path}')
            return False

    @staticmethod
    def mig_root_check():
        """
        Check if MigVisma folder exists.
        :return: True if MigVisma folder exists
        :rtype: bool
        """
        if os.path.exists(cfg.MIG_ROOT):
            return True
        else:
            logging.error(msg=f' MigVisma path {cfg.PENTAHO_DIR} doesnt exist')
            return False

    def customer_dir_check(self):
        """
        Check if customer directory path exists.
        :return: True if customer directory path exists
        :rtype: bool
        """
        customer_folder = os.path.join(cfg.MIG_ROOT, self.customer_dir)
        if os.path.exists(customer_folder):
            return True
        else:
            logging.critical(msg=f' Customer directory doesnt exist in {customer_folder}')
            return False

    def mig_type_dir_check(self):
        """
        Check if {migration_type} folder exists inside customer folder.
        NOTE: There should always be a folder inside customer folder called as migration type (PDOL, SDOL, MLM, etc..).
        :return: True if {migration_type} folder exists
        :rtype: bool
        """
        if os.path.exists(os.path.join(cfg.MIG_ROOT, self.customer_dir, self.mig_type)):
            return True
        else:
            return False

    def not_reserved_check(self):
        """
        Check if customer dir name is not in reserved names list stored in config.py script.
        :return: True if customer directory name is NOT in reserved names list
        :rtype: bool
        """
        if self.customer_dir not in cfg.RESERVED_DIRS:
            return True
        else:
            logging.critical(msg=f' Customer folder {self.customer_dir} is in the reserved list')
            return False

    def props_check(self):
        """
        Check if config.properties file exists in customer folder.
        NOTE: it's a mandatory file for successful migration
        :return: True if config.properties file exists
        :rtype: bool
        """
        props_path = os.path.join(cfg.MIG_ROOT, self.customer_dir, 'config.properties')
        if os.path.isfile(props_path):
            return True
        else:
            logging.warning(msg=f" File config.properties doesn't exist in {self.customer_dir} folder")
            logging.info(msg=f" This is not mandatory check for PDOL and SDOL anymore based on the new requirements")
            return False

    def params_check(self):
        """
        Check if MigVisma_parameters.xlsx file exists in customer folder.
         NOTE: it's a mandatory file for successful migration
        :return: True if MigVisma_parameters.xlsx file exists
        :rtype: bool
        """
        params_path = os.path.join(cfg.MIG_ROOT, self.customer_dir, 'MigVisma_parameters.xlsx')

        if os.path.isfile(params_path):
            return True
        else:
            logging.critical(msg=f" File MigVisma_parameters.xlsx doesn't exist in {self.customer_dir} folder")
            return False

    def mig_params_xlsx_check(self):
        """
        Check if:
        1) PDOL_parameters.xlsx
        2) SDOL_parameters.xlsx
        3) MLM_parameters.xlsx
        file exists in customer folder - depends on the migration type
        :return:
        """
        mig_params_path = os.path.join(cfg.MIG_ROOT, self.customer_dir, self.mig_type, f'{self.mig_type}_parameters.xlsx')

        if os.path.isfile(mig_params_path):
            return True
        else:
            logging.critical(msg=f" File {self.mig_type}_parameters.xlsx doesn't exist in {self.customer_dir} folder")
            return False
