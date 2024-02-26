mod player;

fn main(){
    player::play_movie("snatch.mp4");
    player::play_audio("rhcp.mp3");

    clean::perform_clean();
    clean::files::clean_files()
}

mod clean {
    pub fn perform_clean() {
        println!("Cleaning hdd");
    }

    pub mod files {
        pub fn clean_files() {
            println!("Removing unused files");
        }
    }
}