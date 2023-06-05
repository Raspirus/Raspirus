#[cfg(test)]
mod tests {
    use crate::backend::config_file::Config;

    #[test]
    fn test_new_config() {
        let config = Config::new();

        assert_eq!(config.hashes_in_db, 0);
        assert_eq!(config.last_db_update, "Never");
        assert_eq!(config.logging_is_active, false);
        assert_eq!(config.obfuscated_is_active, true);
        assert_eq!(config.db_update_weekday, -1);
        assert_eq!(config.db_update_time, "22:00:00");
    }

    #[test]
    fn test_save_and_load_config() {
        let config = Config {
            hashes_in_db: 10,
            last_db_update: "2023-06-05".to_string(),
            logging_is_active: true,
            obfuscated_is_active: false,
            db_update_weekday: 2,
            db_update_time: "08:00:00".to_string(),
        };

        let result_save = config.save();
        assert!(result_save.is_ok());

        let loaded_config = Config::new();
        let result_load = loaded_config.load();
        assert!(result_load.is_ok());

        let loaded_config = result_load.unwrap();
        assert_eq!(loaded_config.hashes_in_db, config.hashes_in_db);
        assert_eq!(loaded_config.last_db_update, config.last_db_update);
        assert_eq!(loaded_config.logging_is_active, config.logging_is_active);
        assert_eq!(loaded_config.obfuscated_is_active, config.obfuscated_is_active);
        assert_eq!(loaded_config.db_update_weekday, config.db_update_weekday);
        assert_eq!(loaded_config.db_update_time, config.db_update_time);
    }
}