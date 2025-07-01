class Solution {
    fun findItinerary(tickets: List<List<String>>): List<String> {
        val routes = mutableMapOf<String, PriorityQueue<String>>()
        for (ticket in tickets) {
            val frm = ticket[0]
            val to = ticket[1]
            val tos = routes.getOrPut(frm) { PriorityQueue<String>() }
            tos.add(to)
        }

        val res = mutableListOf<String>()
        fun findroute(stop: String) {
            while (routes[stop]?.isNotEmpty() == true) {
                val to = routes[stop]!!.poll()
                findroute(to)
            }
            res.add(stop)
        }
        findroute("JFK")
        res.reverse()
        return res
    }
}
