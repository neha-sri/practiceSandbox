class Solution {
    class Project implements Comparable<Project>{
        private int capital;
        private int profit;

        public Project(int capital, int profit){
            this.capital = capital;
            this.profit = profit;
        }

        @Override
        public int compareTo(Project p){
            return this.capital - p.capital;
        }

    }
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {

        Project[] projects = new Project[capital.length];
        for(int i=0; i<capital.length; i++){
            projects[i] = new Project(capital[i], profits[i]);
        }
        
        Arrays.sort(projects, (a,b) -> a.capital > b.capital ? 1 : a.capital == b.capital? 0: -1);

        int investments = 0;
        int index = 0;

        PriorityQueue<Integer> profitMaxHeap = new PriorityQueue<Integer>((a,b) -> b - a);
        while(investments < k){
            while(index < projects.length && projects[index].capital <= w){
                profitMaxHeap.add(projects[index].profit);
                index++;
            }

            if(profitMaxHeap.isEmpty()) {
                break;
            }

            investments++;
            w = w + profitMaxHeap.poll();
        }

        return w;
    }
}
