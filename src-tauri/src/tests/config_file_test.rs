#[cfg(test)]
mod tests {
    use crate::backend::config_file::Config;

    #[test]
    fn test_new_config() {
        let config = Config::new().unwrap();

        assert_eq!(config.hashes_in_db, 0);
        assert_eq!(config.last_db_update, "Never");
        assert!(!config.logging_is_active);
        assert!(config.obfuscated_is_active);
        assert_eq!(config.db_location, "");
        assert!(config.scan_dir);
        assert_eq!(config.ignored_hashes, Vec::<String>::new());
    }

    #[test]
    fn test_save_and_load_config() {
        let config = Config::new();
        assert!(config.is_ok());
        let mut config_clean = config.unwrap();
        config_clean.hashes_in_db = 10;
        config_clean.last_db_update = "2023-06-05".to_string();
        config_clean.logging_is_active = true;
        config_clean.obfuscated_is_active = false;
        config_clean.db_location = "".to_string();
        config_clean.scan_dir = true;
        config_clean.ignored_hashes = Vec::new();

        let result_save = config_clean.save();
        assert!(result_save.is_ok());

        let loaded_config = Config::new();
        assert!(loaded_config.is_ok());

        let loaded_config = loaded_config.unwrap();
        assert_eq!(loaded_config.hashes_in_db, config_clean.hashes_in_db);
        assert_eq!(loaded_config.last_db_update, config_clean.last_db_update);
        assert_eq!(
            loaded_config.logging_is_active,
            config_clean.logging_is_active
        );
        assert_eq!(
            loaded_config.obfuscated_is_active,
            config_clean.obfuscated_is_active
        );
        assert_eq!(loaded_config.db_location, config_clean.db_location);
        assert_eq!(loaded_config.scan_dir, config_clean.scan_dir);
        assert_eq!(loaded_config.ignored_hashes, config_clean.ignored_hashes);
    }
}
