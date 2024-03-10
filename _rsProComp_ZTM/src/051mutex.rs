use crossbeam_channel::{unbounded, Receiver, Sender};
use parking_lot::Mutex;
use std::collections::VecDeque;
use std::sync::Arc;
use std::thread::{self, JoinHandle};
use std::time::Duration;
#[derive(Clone)]
enum Job {
    Print(String),
    Sum(isize, isize),
}

#[derive(Clone)]
enum Message {
    AddJob(Job),
    Quit,
}
struct Worker<M> {
    tx: Sender<M>,
    _rx: Receiver<M>,
    handle: JoinHandle<()>,
}

impl Worker<Message> {
    fn add_job(&self, job: Job) {
        self.tx
            .send(Message::AddJob(job))
            .expect("Failed to add job");
    }
    fn join(self) {
        self.handle.join().expect("failed to join thread");
    }
    fn send_msg(&self, msg: Message) {
        self.tx.send(msg).expect("failed to send message");
    }
}

fn spawn_worker(counter: Arc<Mutex<usize>>) -> Worker<Message> {
    let (tx, rx) = unbounded();
    let rx_thread = rx.clone();
    let handle = thread::spawn(move || {
        let mut jobs = VecDeque::new();
        loop {
            loop {
                for job in jobs.pop_front() {
                    match job {
                        Job::Print(msg) => println!("{}", msg),
                        Job::Sum(lhr, rhs) => println!("{}+{}={}", lhr, rhs, (lhr + rhs)),
                    }
                    let mut counter = counter.lock();
                    *counter += 1;
                }
                if let Ok(msg) = rx_thread.try_recv() {
                    match msg {
                        Message::AddJob(job) => {
                            jobs.push_back(job);
                            continue;
                        }
                        Message::Quit => return,
                    }
                } else {
                    break;
                }
            }
            thread::sleep(Duration::from_millis(100));
        }
    });
    Worker {
        tx,
        _rx: rx,
        handle,
    }
}

fn main() {
    let jobs = vec![
        Job::Print("hello".to_owned()),
        Job::Sum(2, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(5, 3),
        Job::Print("hello".to_owned()),
        Job::Sum(2, 1),
        Job::Print("hello".to_owned()),
        Job::Sum(5, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(7, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(2, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(3, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(4, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(9, 2),
        Job::Print("hello".to_owned()),
        Job::Sum(8, 2),
    ];

    let jobs_sent = jobs.len();
    let job_counter = Arc::new(Mutex::new(0));
    let mut workers = vec![];
    for _ in 0..4 {
        let worker = spawn_worker(Arc::clone(&job_counter));
        workers.push(worker);
    }

    let mut worker_ring = workers.iter().cycle();
    for job in jobs.into_iter() {
        let worker = worker_ring.next().expect("failed to get next worker");
        worker.add_job(job);
    }
    for worker in &workers {
        worker.send_msg(Message::Quit);
    }
    for worker in workers {
        worker.join();
    }
}
