import videoBg from './assets/pexels-mart-production-8121440 (2160p).mp4'

const Bg = () => {
    return (
        <div>
            <video src={videoBg} autoPlay loop muted/>
        </div>
    )
}

export default Bg