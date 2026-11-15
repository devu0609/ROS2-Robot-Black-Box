from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy
)


def make_qos(reliability, durability, depth):

    rel = (
        ReliabilityPolicy.RELIABLE
        if reliability == 'reliable'
        else ReliabilityPolicy.BEST_EFFORT
    )

    dur = (
        DurabilityPolicy.TRANSIENT_LOCAL
        if durability == 'transient_local'
        else DurabilityPolicy.VOLATILE
    )

    return QoSProfile(
        reliability=rel,
        durability=dur,
        history=HistoryPolicy.KEEP_LAST,
        depth=depth
    )
