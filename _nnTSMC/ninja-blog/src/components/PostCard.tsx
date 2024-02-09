export default function PostCard({title, author}: {title: string, author: string}) {
    return (
        <div className="card">
            <h2>{title}</h2>
            <p>Written By {author}</p>
        </div>
    )
}