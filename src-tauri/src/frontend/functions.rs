use log::{debug, error, info, warn};

use crate::backend::utils;

#[cfg(all(not(debug_assertions), windows))]
pub fn remove_windows_console() {
    unsafe {
        windows_sys::Win32::System::Console::FreeConsole();
    }
}

// If a command is not yet implemented
pub fn not_implemented(app: tauri::AppHandle) {
    warn!("Function not implemented yet");
    app.exit(2);
}

// Starts the GUI without attaching a CLI
pub fn cli_gui(app: tauri::AppHandle) -> Result<(), tauri::Error> {
    debug!("Showing GUI...");
    #[cfg(all(not(debug_assertions), windows))]
    remove_windows_console();
    tauri::WebviewWindowBuilder::new(
        &app,
        "raspirus",
        tauri::WebviewUrl::App("index.html".into()),
    )
    .title("Raspirus")
    .inner_size(800., 480.)
    .resizable(true)
    .build()?;
    debug!("This won't show on Windows release builds");
    Ok(())
}

// Starts the scanner on the CLI
pub fn cli_scanner(app: tauri::AppHandle, data: String) {
    let unescaped_str = data.replace("\\n", "\n").replace("\\t", "\t");
    debug!("Data provided: {}", unescaped_str);
    match utils::scanner_utils::start_scanner(None, unescaped_str) {
        Ok(res) => {
            info!("Result: {res}");
            app.exit(0);
        }
        Err(err) => {
            error!("Error: {err}");
            app.exit(-1);
        }
    }
}

// Updates the DB over the CLI
pub fn cli_dbupdate(app: tauri::AppHandle) {
    match utils::update_utils::update(None) {
        Ok(res) => {
            info!("Result: {res}");
            app.exit(0);
        }
        Err(err) => {
            error!("Error: {err}");
            app.exit(-1);
        }
    }
}
